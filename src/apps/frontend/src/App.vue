<template>
  <header>
    <h1>Hefesto</h1>
  </header>
  <h2>Log in</h2>
  <button @click="googleSignIn">
    Log in with Google
  </button>
</template>
<script>
import { initializeApp } from "firebase/app"
import { getAuth, signInWithPopup, GoogleAuthProvider } from "firebase/auth"

const app = initializeApp({
  apiKey: "AIzaSyBNFRY0nCu2m9oyuoV6a2dPUitL7hwpWM8",
  authDomain: "hefesto-front.firebaseapp.com",
  projectId: "hefesto-front",
  storageBucket: "hefesto-front.appspot.com",
  messagingSenderId: "555862128122",
  appId: "1:555862128122:web:5169d027330b34667d6043"
})


export default {
  name: 'SignUp',
  methods: {
    googleSignIn: async function () {
      const provider = new GoogleAuthProvider()
      const auth = getAuth(app)

      try {
        const credentials = await signInWithPopup(auth, provider)
        console.log('credentials', credentials)
        const token = credentials.user.accessToken
        
        const response = await fetch('http://127.0.0.1:8080/login', {
          method: "POST",
          headers: { Authentication: `Bearer ${token}` }
        })

        console.log(response)
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
<style scoped></style>
