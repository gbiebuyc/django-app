<template>
  <div>
        <div
            @click="nodeClicked"
            :style="{'margin-left': `${depth * 20}px`}"
            class="node">
            <span 
                v-if="hasChildren"
                class="type"
            >{{expanded ? '&#9660;' : '&#9658;'}}</span>
            <span class="type" v-else>&#9671;</span>
            <span>{{ node.name }}</span>
        </div>
        <div v-if="expanded">
            <TreeBrowser
                v-for="child in node.children"
                :key="child.name"
                :node="child"
                :depth="depth + 1"
                @onClick="node => $emit('onClick', node)"
            />
        </div>
  </div>
</template>

<script>
export default {
  name: "TreeBrowser",
  props: {
    node: Object,
    depth: {
        type: Number,
        default: 0,
    },
    initialExpanded: {
        type: Boolean,
        default: false,
    }
  },
  data () {
      return {
          expanded: this.initialExpanded,
      }
  },
  computed: {
      hasChildren() {
          return this.node.children;
      }
  },
  methods: {
      nodeClicked() {
          this.expanded = !this.expanded;
          if (!this.hasChildren) {
              this.$emit('onClick', this.node)
          }
      }
  }
};
</script>

<style scoped>
.node {
    text-align: left;
    font-size: 18px;
    user-select: none;
}

.node:hover {
    color: #42b983;
}

.type {
    margin-right: 10px;
}
</style>
