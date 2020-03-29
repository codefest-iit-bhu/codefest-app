import { KEY_AUTH_TOKEN } from '@js/constants.js'
import API, { Response, STATUS } from '@js/api.js'

import firebase from 'firebase'
const localStorage = process.browser
  ? window.localStorage
  : {
      getItem() {},
      setItem() {},
      removeItem() {}
    }

function getTokenFromStorage() {
  return localStorage.getItem(KEY_AUTH_TOKEN)
}

function putTokenToStorage(token) {
  if (!token) localStorage.removeItem(KEY_AUTH_TOKEN)
  else localStorage.setItem(KEY_AUTH_TOKEN, token)
}

export const state = () => ({
  token: getTokenFromStorage() || '',
  userId: -1
})

export const mutations = {
  AUTH_SUCCESS(state, data) {
    const { token, user_id } = data
    state.token = token
    state.userId = user_id
    putTokenToStorage(token)
  },
  AUTH_LOGOUT(state) {
    state.token = ''
    putTokenToStorage(null)
  }
}

export const getters = {
  isLoggedIn: (state) => {
    return !!state.token
  },
  authToken: (state) => state.token
}

export const actions = {
  login({ state, commit }, { idToken }) {
    const body = {
      id_token: idToken
    }
    return API.post('login/', { body }).then((response) => {
      commit('AUTH_SUCCESS', response.data)
      return response
    })
  },
  register({ state, commit }, { idToken, name, referralCode, recaptchaToken }) {
    const names = name.split(/\s+/)
    const body = {
      id_token: idToken,
      first_name: names[0],
      last_name: names.length > 0 ? names[1] : '',
      applied_referral_code: referralCode,
      g_recaptcha_response: recaptchaToken
    }
    return API.post('register/', { body }).then((response) => {
      commit('AUTH_SUCCESS', response.data)
      return response
    })
  },
  logout({ state, commit }) {
    firebase.auth().signOut()
    commit('AUTH_LOGOUT')
  }
}
