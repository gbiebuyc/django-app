<template>
  <div class="home">
    <h1>Home</h1>
    <ul v-if="companies.length">
      <li v-for="c in companies" :key="c.url">
        <router-link to="">{{ c.name }}</router-link>
      </li>
    </ul>
    <p v-else>no companies</p>
  </div>
</template>

<script>
export default {
  name: 'home',
  props: ['userprofile'],
  computed: {
    companies: function () {
      if (!this.userprofile)
        return {};
      return this.userprofile.profile.company;
    }
  },
};
</script>

<style scoped>

</style>
