<template>
  <div id="app">
    <b-navbar type="light" variant="light">
      <div class="container">
        <b-navbar-brand to="/">
          <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAA8CAYAAAD/jkPjAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQ1IDc5LjE2MzQ5OSwgMjAxOC8wOC8xMy0xNjo0MDoyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MEM0QUFENjAxNUJEMTFFOTk4QjhEMDgzQjQ2MjA5NDMiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MEM0QUFENjExNUJEMTFFOTk4QjhEMDgzQjQ2MjA5NDMiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDowQzRBQUQ1RTE1QkQxMUU5OThCOEQwODNCNDYyMDk0MyIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDowQzRBQUQ1RjE1QkQxMUU5OThCOEQwODNCNDYyMDk0MyIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Powl160AABKoSURBVHja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" alt="logo">
        </b-navbar-brand>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item v-if="userdata && userdata.is_staff" href="/admin/" v-b-tooltip.hover title="Admin site"><font-awesome-icon icon="user-cog" /></b-nav-item>

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
      <router-view v-else :userdata="userdata" @fetchData="fetchData"/>
    </div>
    <b-modal id="notyetimplemented" title=":(" centered ok-only>Not yet implemented</b-modal>
  </div>
</template>

<script>
import { CSRF_TOKEN } from "@/common/csrf_token.js";
export default {
  data() {
    return {
      userdata: null,
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
      }).then(resp => {
        return resp.json();
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
        })
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
  margin: 0 5px;
}
</style>
