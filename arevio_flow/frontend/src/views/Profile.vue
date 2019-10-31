<template>
  <div class="profile pt-3">
    <b-card img-src="https://placekitten.com/300/300" img-alt="Card image" img-left class="mb-3">
      <b-card-text>
        <h1>your profile</h1>
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
