<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <!-- <router-link to="/annualreport">Annual Report</router-link> | -->
      <router-link to="/profile">Profile</router-link> |
      <a href="/accounts/logout/">Logout</a>
      <span v-if="userprofile && userprofile.is_staff"> |
        <a href="/admin/">Admin site</a>
      </span>
    </div>
    <router-view id="main" :userprofile="userprofile"/>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  data() {
    return {
      userprofile: null,
    };
  },
  methods: {
  },
  created() {
    apiService('/api/users/me/')
      .then(data => {
        this.userprofile = data;
      })
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  position: fixed;
  width: 100%;
  top: 0px;
  left: 0px;
  padding: 30px;
  box-shadow: 0 0 1px rgba(0,0,0,0.25);
  background-color: white;
  z-index: 100;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#main {
  position: absolute;
  top: 80px;
  left: 0px;
  width: 100%;
}
.error {
  color: darkred;
  text-align: center;
}
</style>
