(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["profile"],{"36e8":function(e,t,n){"use strict";n.r(t);var c=n("7a23"),r=n("dad5"),o=n("2906"),u=function(e){return Object(c["pushScopeId"])("data-v-163d82f7"),e=e(),Object(c["popScopeId"])(),e},a={key:0,id:"profile",class:"container view"},s=u((function(){return Object(c["createElementVNode"])("div",{id:"bottom"},null,-1)})),d=Object(c["defineComponent"])({setup:function(e){var t=Object(o["a"])(),n=Object(c["computed"])((function(){return t.getters[r["a"].GETTERS.AUTH_USER_PROFILE]}));return function(e,t){var r=Object(c["resolveComponent"])("router-view");return Object(c["unref"])(n).username?(Object(c["openBlock"])(),Object(c["createElementBlock"])("div",a,[Object(c["createVNode"])(r,{user:Object(c["unref"])(n)},null,8,["user"]),s])):Object(c["createCommentVNode"])("",!0)}}}),i=(n("9674"),n("6b0d")),b=n.n(i);const f=b()(d,[["__scopeId","data-v-163d82f7"]]);t["default"]=f},"3ba8":function(e,t,n){"use strict";n("a020")},9674:function(e,t,n){"use strict";n("b64c")},a020:function(e,t,n){},ad3d:function(e,t,n){"use strict";n.r(t);var c=n("7a23"),r=n("6c02"),o=n("3c44"),u=n("71a7"),a=n("dad5"),s=n("2906"),d={key:0,id:"user",class:"view"},i={class:"box"},b=Object(c["defineComponent"])({setup:function(e){var t=Object(r["c"])(),n=Object(s["a"])(),b=Object(c["computed"])((function(){return n.getters[a["e"].GETTERS.USER]}));return Object(c["onBeforeMount"])((function(){t.params.username&&"string"===typeof t.params.username&&n.dispatch(a["e"].ACTIONS.GET_USER,t.params.username)})),Object(c["onBeforeUnmount"])((function(){n.dispatch(a["e"].ACTIONS.EMPTY_USER)})),function(e,t){return Object(c["unref"])(b).username?(Object(c["openBlock"])(),Object(c["createElementBlock"])("div",d,[Object(c["createVNode"])(o["a"],{user:Object(c["unref"])(b)},null,8,["user"]),Object(c["createElementVNode"])("div",i,[Object(c["createVNode"])(u["a"],{user:Object(c["unref"])(b),"from-admin":!0},null,8,["user"])])])):Object(c["createCommentVNode"])("",!0)}}}),f=(n("3ba8"),n("6b0d")),O=n.n(f);const p=O()(b,[["__scopeId","data-v-10e7b479"]]);t["default"]=p},b64c:function(e,t,n){}}]);
//# sourceMappingURL=profile.d25975e2.js.map