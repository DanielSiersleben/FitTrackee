from typing import Dict, Union

from flask import Blueprint, request

from fittrackee.federation.exceptions import RemoteActorException
from fittrackee.federation.utils_user import create_remote_user
from fittrackee.responses import (
    HttpResponse,
    InvalidPayloadErrorResponse,
    UserNotFoundErrorResponse,
)
from fittrackee.users.decorators import authenticate

from .decorators import federation_required
from .inbox import inbox
from .models import Actor, Domain

ap_federation_blueprint = Blueprint('ap_federation', __name__)


@ap_federation_blueprint.route(
    '/user/<string:preferred_username>', methods=['GET']
)
@federation_required
def get_actor(app_domain: Domain, preferred_username: str) -> HttpResponse:
    """
    Get a local actor

    **Example request**:

    .. sourcecode:: http

      GET /federation/user/admin HTTP/1.1
      Content-Type: application/json

    **Example response**:

    .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/jrd+json; charset=utf-8

      {
        "@context": [
          "https://www.w3.org/ns/activitystreams",
          "https://w3id.org/security/v1"
        ],
        "id": "https://example.com/federation/user/Sam",
        "type": "Person",
        "preferredUsername": "Sam",
        "name": "Sam",
        "url": "https://example.com/users/Sam",
        "inbox": "https://example.com/federation/user/Sam/inbox",
        "outbox": "https://example.com/federation/user/Sam/outbox",
        "followers": "https://example.com/federation/user/Sam/followers",
        "following": "https://example.com/federation/user/Sam/following",
        "manuallyApprovesFollowers": true,
        "publicKey": {
          "id": "https://example.com/federation/user/Sam#main-key",
          "owner": "https://example.com/federation/user/Sam",
          "publicKeyPem": "-----BEGIN PUBLIC KEY---(...)---END PUBLIC KEY-----"
        },
        "endpoints": {
          "sharedInbox": "https://example.com/federation/inbox"
        }
      }

    :param string preferred_username: actor preferred username

    :statuscode 200: success
    :statuscode 403: Error. Federation is disabled for this instance.
    :statuscode 404: User does not exist.

    """
    actor = Actor.query.filter_by(
        preferred_username=preferred_username,
        domain_id=app_domain.id,
    ).first()
    if not actor:
        return UserNotFoundErrorResponse()

    return HttpResponse(
        response=actor.serialize(),
        content_type='application/jrd+json; charset=utf-8',
    )


@ap_federation_blueprint.route('/remote-user', methods=['POST'])
@federation_required
@authenticate
def remote_actor(
    app_domain: Domain, auth_user_id: int
) -> Union[Dict, HttpResponse]:
    """
    Add a remote actor to local instance if it does not exist.
    Otherwise it updates it.

    **Example request**:

    .. sourcecode:: http

      POST /federation/remote_user HTTP/1.1
      Content-Type: application/json

    **Example response**:

    .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/jrd+json; charset=utf-8

      {
        "@context": [
          "https://www.w3.org/ns/activitystreams",
          "https://w3id.org/security/v1"
        ],
        "id": "https://remote-instance.social/user/Sam",
        "type": "Person",
        "preferredUsername": "Sam",
        "name": "Sam",
        "url": "https://remote-instance.social/@Sam",
        "inbox": "https://remote-instance.social/user/Sam/inbox",
        "outbox": "https://remote-instance.social/user/Sam/outbox",
        "followers": "https://remote-instance.social/user/Sam/followers",
        "following": "https://remote-instance.social/user/Sam/following",
        "manuallyApprovesFollowers": true,
        "publicKey": {
          "id": "https://remote-instance.social/user/Sam#main-key",
          "owner": "https://remote-instance.social/user/Sam",
          "publicKeyPem": "-----BEGIN PUBLIC KEY---(...)---END PUBLIC KEY-----"
        },
        "endpoints": {
          "sharedInbox": "https://remote-instance.social/inbox"
        }
      }

    :param integer auth_user_id: authenticate user id (from JSON Web Token)

    :<json string actor_url: remote actor activitypub id

    :reqheader Authorization: OAuth 2.0 Bearer Token

    :statuscode 200: success
    :statuscode 400:
      - Invalid payload.
      - The provided account is not a remote account.
      - Can not fetch remote actor.
      - Invalid remote actor object.
    :statuscode 401:
        - Provide a valid auth token.
        - Signature expired. Please log in again.
        - Invalid token. Please log in again.
    :statuscode 403: Error. Federation is disabled for this instance.

    """
    remote_actor_url = (
        request.get_json(silent=True).get('actor_url')  # type: ignore
        if request.get_json(silent=True) is not None
        else None
    )
    try:
        actor = create_remote_user(remote_actor_url)
    except RemoteActorException as e:
        return InvalidPayloadErrorResponse(e.message)
    return HttpResponse(
        response=actor.serialize(),
        content_type='application/jrd+json; charset=utf-8',
    )


@ap_federation_blueprint.route(
    '/user/<string:preferred_username>/inbox', methods=['POST']
)
@federation_required
def user_inbox(
    app_domain: Domain, preferred_username: str
) -> Union[Dict, HttpResponse]:
    """
    Post an activity to user inbox

    **Example request**:

    .. sourcecode:: http

      POST /federation/user/Sam/inbox HTTP/1.1
      Content-Type: application/json

    **Example response**:

    .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "status": "success"
      }

    :param string preferred_username: actor preferred username

    :<json json activity: activity

    :statuscode 200: success
    :statuscode 400: Invalid payload.
    :statuscode 403: Error. Federation is disabled for this instance.
    :statuscode 404: User does not exist.

    """
    return inbox(request, app_domain, preferred_username)
