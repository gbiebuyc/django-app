<template>
  <div class="home" style="padding: 20px;">
    <h1>Home</h1>
    <div v-if="companies.length" class="card-columns">
      <div v-for="c in companies" :key="c.url" class="card">
        <img src="https://www.royalcontainers.com/wp-content/uploads/2017/03/logo-placeholder.jpeg" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">{{ c.name }}</h5>
          <router-link class="stretched-link" to=""></router-link>
        </div>
      </div>
    </div>
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
