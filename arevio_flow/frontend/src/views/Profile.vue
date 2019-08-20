<template>
  <div class="profile">
    <h1>your profile</h1>
    <p>{{ userprofile }}</p>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: 'profile',
  data() {
    return {
      userprofile: null,
    };
  },
  methods: {
  },
  created() {
    apiService('/api/me/')
      .then(data => {
        this.userprofile = data;
      })
  },
};
</script>

<style scoped>

</style>
