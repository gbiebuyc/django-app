<template>
  <div id="app">
    <b-navbar type="light" variant="light">
      <div class="container">
        <b-navbar-brand to="/">
          <img src="/static/arevio-branding-logo.png" alt="logo" v-b-tooltip.hover title="Home">
        </b-navbar-brand>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item v-if="userdata && userdata.is_superuser" href="/admin/" v-b-tooltip.hover title="Admin site"><font-awesome-icon icon="user-cog" /></b-nav-item>

          <b-nav-item-dropdown right>
            <template v-slot:button-content>
              <font-awesome-icon icon="language" />
            </template>
            <b-dropdown-item href="#" v-b-modal.notyetimplemented>EN</b-dropdown-item>
            <b-dropdown-item href="#" v-b-modal.notyetimplemented>ES</b-dropdown-item>
            <b-dropdown-item href="#" v-b-modal.notyetimplemented>RU</b-dropdown-item>
            <b-dropdown-item href="#" v-b-modal.notyetimplemented>FA</b-dropdown-item>
          </b-nav-item-dropdown>

          <b-nav-item-dropdown right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <font-awesome-icon icon="user-circle" />
              <span style="font-size: 1rem; position: relative; bottom: 3px"> {{ userdata ? userdata.username : '' }} </span>
            </template>
            <b-dropdown-item to="/profile">Profile</b-dropdown-item>
            <b-dropdown-item href="/accounts/logout/">Sign Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </div>
    </b-navbar>
    <div class="container p-0">
      <p v-if="loading" class="pt-3">Loading...</p>
      <router-view v-else :userdata="userdata" @fetchData="fetchData" @handleError="handleError"/>
    </div>
    <div class="footer" style="border-top: 1px solid #eceef1;"></div>
    <div class="container p-0 footer">
      <div style="display: flex; flex-direction: row; align-items: center; height: 100%; width: 100%">
        <img src="/static/acsone-logo.png" width="100px">
        <div style="display: flex; flex-direction: column; align-items: flex-end; width: 100%">
          <p class="m-0 text-secondary">Copyright ©&nbsp;2019 ACSONE SA/NV</p>
        </div>
      </div>
    </div>

    <b-modal id="notyetimplemented" title=":(" centered ok-only>Not yet implemented</b-modal>

    <b-modal id="error"
      :title="error && error.name"
      header-text-variant="danger"
      centered
      hide-footer
    > <p>{{ error && error.message }}</p>
    </b-modal>

  </div>
</template>

<script>
import { CSRF_TOKEN } from "@/common/csrf_token.js";
export default {
  data() {
    return {
      userdata: null,
      error: null,
    };
  },
  computed: {
    loading: function () {
      return (this.userdata === null) ? true : false;
    },
  },
  methods: {
    fetchData: function () {
      fetch('/userdata/', {
        method: 'GET',
        headers: {'X-CSRFTOKEN': CSRF_TOKEN},
      }).then(response => {
        if (!response.ok) throw response;
        return response.json();
      }).then(data => {
          data.taxonomyNames = [];
          data.taxonomies.forEach(item => {
            data.taxonomyNames[item.id] = item.name;
          });
          if (!data.companies.length) {
            data.companies = [{ value: null, text: 'Please select a company'},];
          } else {
            let tmp = [];
            data.companies.forEach(item => {
              tmp.push({
                value: item,
                text: item.name,
              });
            });
            data.companies = tmp;
          }
          this.userdata = data;
        }).catch(error => this.handleError(error));
    },
    handleError(error) {
      if (error instanceof Response) {
        error.text().then(text => {
          this.error = {
            name: `HTTP ${error.status} ${error.statusText}`,
            message: text,
          };
          this.$bvModal.hide('spinner-modal');
          this.$bvModal.show('error');
        });
      } else {
        if (error.message == 'Failed to fetch') {
          this.error = {
            name: 'Network error',
            message: 'Check your internet connection.'
          };
        } else {
          this.error = error;
        }
        this.$bvModal.hide('spinner-modal');
        this.$bvModal.show('error');
      }
    },
  },
  created() {
    this.fetchData();
  },
};
</script>

<style>
.error {
  color: darkred;
  text-align: center;
}
nav > div > ul > li > a {
  font-size: 1.3rem;
  margin-left: 10px;
}
/* Sticky footer styles
-------------------------------------------------- */
html {
  position: relative;
  min-height: 100%;
}
body {
  margin-bottom: 80px; /* footer height */
}
.footer {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 80px; /* footer height */
}
</style>
