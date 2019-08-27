<template>
  <div class="annualreport">
    <div class="TreeBrowser">
      <TreeBrowser
        :node="root"
        :initialExpanded="true"
        @onClick="nodeWasClicked"
      />
    </div>
    <NodeDetail class="NodeDetail" :node="selectedNode"/>
  </div>
</template>

<script>
// @ is an alias to /src
import TreeBrowser from "@/components/TreeBrowser.vue";
import NodeDetail from "@/components/NodeDetail.vue";
import root from "@/root.json";

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
    };
  },
  methods: {
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
    }
  }
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
