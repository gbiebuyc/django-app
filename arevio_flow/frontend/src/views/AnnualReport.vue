<template>
  <div class="annualreport">
    <p v-if="loading">Loading...</p>
    <div v-else>
      <div class="TreeBrowser">
        <b-button v-b-modal.modal-1 @click="showSuccessAlert = false;">Taxonomy package</b-button>
        <TreeBrowser
          :node="root"
          :initialExpanded="true"
          @onClick="nodeWasClicked"
        />
      </div>
      <NodeDetail class="NodeDetail" :node="selectedNode"/>
      <b-modal id="modal-1" title="Taxonomy Package" ok-only>
        <p>Current taxonomy package: <strong>{{currentTaxonomyName}}</strong></p>
        <form @submit="submitTaxonomy">
          <p><input type="file" ref="fileInput"></p>
          <p><input type="submit"></p>
        </form>
        <b-alert :show="showSuccessAlert" variant="success" fade>File updated successfully</b-alert>
      </b-modal>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import TreeBrowser from "@/components/TreeBrowser.vue";
import NodeDetail from "@/components/NodeDetail.vue";
import root from "@/root.json";
import { apiService } from "@/common/api.service.js";
import { CSRF_TOKEN } from "@/common/csrf_token.js";

export default {
  name: 'annualreport',
  components: {
    TreeBrowser,
    NodeDetail,
  },
  data() {
    return {
      root,
      selectedNode: null,
      report: null,
      showSuccessAlert: false,
    };
  },
  methods: {
    fetchData: function () {
      apiService(`/api/annualreports/${this.$route.params.id}/`)
        .then(data => {this.report = data});
    },
    submitTaxonomy: function (e) {
      e.preventDefault();
      let formData = new FormData();
      formData.append('taxonomy', this.$refs.fileInput.files[0] || '');
      fetch(`/api/annualreports/${this.$route.params.id}/`, {
        method: "PATCH",
        headers: {'X-CSRFTOKEN': CSRF_TOKEN,},
        body: formData,
      }).then(response => {
        this.fetchData();
        this.$refs.fileInput.value = "";
        if(!response.ok)
          throw new Error(response.status);
        this.showSuccessAlert = true;
      }).catch((error => console.log(error)));
    },
    nodeWasClicked(node) {
      this.selectedNode = node;
      this.selectedNode.content = [''];
      fetch('https://baconipsum.com/api/?type=meat-and-filler')
        .then(function(response) {
          return response.json();
        })
        .then(myJson => {
          this.selectedNode = {
            name: this.selectedNode.name,
            content: myJson,
          }
        }
      );
    },
  },
  created () {
    this.fetchData();
  },
  computed: {
    loading: function () {
      return (this.report === null) ? true : false;
    },
    currentTaxonomyName: function () {
      if (!this.report.taxonomy)
        return 'empty';
      return this.report.taxonomy.replace(/^.*[\\\/]/, '');
    },
  },
};
</script>

<style scoped>
.TreeBrowser {
  position: fixed;
  overflow-y: scroll;
  top: 80px;
  bottom: 0px;
  left: 0px;
  width: 300px;
  padding: 20px 0 0 20px;
  box-sizing: border-box;
}

.NodeDetail {
  position: absolute;
  left: 300px;
  padding: 20px;
  text-align: left;
}
</style>
