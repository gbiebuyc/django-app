<template>
  <div class="profile pt-3">
    <b-card img-src="https://picsum.photos/id/20/400/400" img-alt="Card image" img-left img-height="200px" class="mt-3">
      <b-card-text>
        <h1>User profile</h1>
        <div class="row mt-3" >
          <div class="col-2" > <h6> Username: </h6> </div>
          <div class="col" > {{ userdata.username }} </div>
        </div>
        <div class="row" >
          <div class="col-2" > <h6> Email: </h6> </div>
          <div class="col" > {{ userdata.email || 'empty' }} </div>
        </div>
        <div class="row" >
          <div class="col-2" > <h6> isAdmin: </h6> </div>
          <div class="col" > {{ userdata.is_staff ? 'true' : 'false' }} </div>
        </div>
      </b-card-text>
    </b-card>
  </div>
</template>

<script>
export default {
  name: 'profile',
  props: ['userdata'],
};
</script>

<style scoped>

</style>
