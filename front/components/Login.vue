<template>
  <div class="text-center">
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn v-if="show" color="indigo accent-4" dark v-bind="attrs" v-on="on">
          <b>ログイン</b>
        </v-btn>
      </template>
      <v-card>
        <v-card-title class="headline indigo accent-4"><b>ログイン</b></v-card-title>
        <v-card-text>
          <v-form>
            <b v-if="error != ''">{{ error }}</b>
            <v-text-field
              prepend-icon="mdi-account-circle"
              v-model="email"
              label="メールアドレス"
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
              singIn();
            "
            style="position:absolute;bottom:10px;right:20px"
          >
            Sign in
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    {{ email }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      dialog: false,
      show: true,
      error: ""
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
            returnSecureToken: true,
          }
        )
        .then(response => {
          console.log(response);
          this.show = false;
          this.dialog = false;
        })
        .catch(error => {
          this.error = error;
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
          this.show = false;
          this.dialog = false;
        })
        .catch(error => {
          this.error = error;
        });
    }
  }
};
</script>
