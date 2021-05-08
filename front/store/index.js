export const state = () => ({
  idToken: null
});
export const mutations = {
  login(state, user) {
    state.user = user;
  },
  logout(state) {
    state.user = null;
  },
  updateIdToken(state, idToken) {
    state.idToken = idToken;
  }
};
export const actions = {};
export const getters = {
  idToken: state => state.idToken
};
