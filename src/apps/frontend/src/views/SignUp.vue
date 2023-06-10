<template>
  <div>
    <div class="about">
      <h1>This is a sign up page</h1>
    </div>
    <button @click="googleSignIn">
      Sign In with Google
    </button>
  </div>
</template>

<script>
import { initializeApp } from "firebase/app"
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth"

const firebaseConfig = {
  apiKey: "AIzaSyBNFRY0nCu2m9oyuoV6a2dPUitL7hwpWM8",
  authDomain: "hefesto-front.firebaseapp.com",
  projectId: "hefesto-front",
  storageBucket: "hefesto-front.appspot.com",
  messagingSenderId: "555862128122",
  appId: "1:555862128122:web:5169d027330b34667d6043"
}

const app = initializeApp(firebaseConfig)
const provider = new GoogleAuthProvider()

export default {
  name: 'SignUp',
  methods: {
    googleSignIn: function () {
      const auth = getAuth(app)

      signInWithPopup(auth, provider)
        .then((result) => {
          console.log('result', result)
          const credential = GoogleAuthProvider.credentialFromResult(result)
          const token = credential.accessToken
          console.log(token)
          console.log('token', token)
          const user = result.user
          console.log('user', user)
        }).catch((error) => {
          const errorCode = error.code
          const errorMessage = error.message
          const email = error.customData.email
          const credential = GoogleAuthProvider.credentialFromError(error)
          console.log(errorCode, errorMessage, email, credential)
        })
    }
  }
}
</script>