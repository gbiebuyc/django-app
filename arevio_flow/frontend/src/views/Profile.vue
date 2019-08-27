<template>
  <div class="profile">
    <h1>your profile</h1>
    <p>{{ userprofile }}</p>
  </div>
</template>

<script>
export default {
  name: 'profile',
  props: ['userprofile'],
};
</script>

<style scoped>

</style>
