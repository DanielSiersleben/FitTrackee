<template>
  <div id="user-preferences" class="description-list">
    <dl>
      <dt>{{ $t('user.PROFILE.LANGUAGE') }}:</dt>
      <dd>{{ language }}</dd>
      <dt>{{ $t('user.PROFILE.TIMEZONE') }}:</dt>
      <dd>{{ timezone }}</dd>
      <dt>{{ $t('user.PROFILE.FIRST_DAY_OF_WEEK') }}:</dt>
      <dd>{{ $t(`user.PROFILE.${fistDayOfWeek}`) }}</dd>
      <dt>{{ $t('user.PROFILE.UNITS.LABEL') }}:</dt>
      <dd>
        {{
          $t(
            `user.PROFILE.UNITS.${user.imperial_units ? 'IMPERIAL' : 'METRIC'}`
          )
        }}
      </dd>
    </dl>
    <div class="profile-buttons">
      <button @click="$router.push('/profile/edit/preferences')">
        {{ $t('user.PROFILE.EDIT_PREFERENCES') }}
      </button>
      <button @click="$router.push('/')">{{ $t('common.HOME') }}</button>
    </div>
  </div>
</template>

<script setup lang="ts">
  import { computed } from 'vue'

  import { IUserProfile } from '@/types/user'
  import { languageLabels } from '@/utils/locales'

  interface Props {
    user: IUserProfile
  }
  const props = defineProps<Props>()

  const language = computed(() =>
    props.user.language
      ? languageLabels[props.user.language]
      : languageLabels['en']
  )
  const fistDayOfWeek = computed(() => (props.user.weekm ? 'MONDAY' : 'SUNDAY'))
  const timezone = computed(() =>
    props.user.timezone ? props.user.timezone : 'Europe/Paris'
  )
</script>
