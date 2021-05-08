<template>
  <v-app>
    <div class="text-center">
      <v-dialog v-model="dialog" width="500">
        <template v-slot:activator="{ on, attrs }">
          <v-btn color="blue lighten-2" dark v-bind="attrs" v-on="on">
            ログイン
          </v-btn>
        </template>
        <v-card>
          <v-card-title class="headline grey lighten-2">ログイン</v-card-title>
          <v-card-text>
            <v-form>
              <v-text-field
                prepend-icon="mdi-account-circle"
                v-model="email"
                label="ユーザ名"
              />
              <v-text-field
                prepend-icon="mdi-account-circle"
                v-model="password"
                label="パスワード"
                type="password"
              />
            </v-form>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions position:relative>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              text
              @click="
                dialog = false;
                singUp();
              "
              style="position:absolute;bottom:10px;right:100px"
            >
              Sign up
            </v-btn>
            <v-btn
              color="primary"
              text
              @click="
                dialog = false;
                singIn();
              "
              style="position:absolute;bottom:10px;right:20px"
            >
              Sign in
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
      {{ email }}{{ password }}
    </div>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      dialog: false
    };
  },
  methods: {
    singUp: function() {
      this.$axios
        .post(
          "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyDLnhjlbZTiwpcJp_x4ssZdrZc7LrxvWHs",
          {
            email: this.email,
            password: this.password,
            returnSecureToken: true
          }
        )
        .then(response => {
          console.log(response);
        });
    },
    singIn: function() {
      this.$axios
        .post(
          "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyDLnhjlbZTiwpcJp_x4ssZdrZc7LrxvWHs",
          {
            email: this.email,
            password: this.password,
            returnSecureToken: true
          }
        )
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>
