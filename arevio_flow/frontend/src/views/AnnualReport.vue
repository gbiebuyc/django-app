<template>
  <div class="annualreport">
    <p v-if="loading">Loading...</p>
    <div v-else>
      <div class="TreeBrowser">
        <b-button v-b-modal.modal-1>Taxonomy package</b-button>
        <TreeBrowser
          :node="root"
          :initialExpanded="true"
          @onClick="nodeWasClicked"
        />
      </div>
      <NodeDetail class="NodeDetail" :node="selectedNode"/>
      <TaxonomyUploadModal :report="report" @fetchData="fetchData"/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import TreeBrowser from "@/components/TreeBrowser.vue";
import NodeDetail from "@/components/NodeDetail.vue";
import root from "@/root.json";
import { apiService } from "@/common/api.service.js";
import TaxonomyUploadModal from "@/components/TaxonomyUploadModal.vue";

export default {
  name: 'annualreport',
  components: {
    TreeBrowser,
    NodeDetail,
    TaxonomyUploadModal,
  },
  data() {
    return {
      root,
      selectedNode: null,
      report: null,
    };
  },
  methods: {
    fetchData: function () {
      apiService(`/api/annualreports/${this.$route.params.id}/`)
        .then(data => {this.report = data});
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
