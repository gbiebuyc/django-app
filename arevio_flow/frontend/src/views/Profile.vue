<template>
  <div class="profile pt-3">
    <div class="position-relative">
      <b-jumbotron>
        <template v-slot:header>
          User profile
        </template>

        <template v-slot:lead>
          <font-awesome-icon icon="user-circle"/>
          <span class="field">{{ userdata.first_name }} {{ userdata.last_name }}</span>
        </template>

        <p><font-awesome-icon icon="envelope"/> <span class="field">{{ userdata.email || 'No email' }}</span></p>
        <p><font-awesome-icon icon="user-shield"/> <span class="field"> {{ userdata.is_superuser ? 'Admin user' : 'Normal user' }}</span></p>
        <b-button variant="primary" href="/accounts/password_change/">Change password</b-button>
      </b-jumbotron>
    </div>
  </div>
</template>

<script>
export default {
  name: 'profile',
  props: ['userdata'],
};
</script>

<style>
.field {
  position: absolute;
  left: 70px;
}
</style>
