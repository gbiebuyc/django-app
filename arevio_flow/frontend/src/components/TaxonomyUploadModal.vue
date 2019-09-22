<template>
  <div>
    <b-modal id="modal-1" title="Taxonomy Package" ok-only @show="showSuccessAlert = false;">
      <p>Current taxonomy package: <strong>{{currentTaxonomyName}}</strong></p>
      <form @submit="submitTaxonomy">
        <p><input type="file" ref="fileInput"></p>
        <p><input type="submit"></p>
      </form>
      <b-alert :show="showSuccessAlert" variant="success" fade>File updated successfully</b-alert>
    </b-modal>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { CSRF_TOKEN } from "@/common/csrf_token.js";

export default {
  name: 'TaxonomyUploadModal',
  props: ['report'],
  data() {
    return {
      showSuccessAlert: false,
    }
  },
  methods: {
    submitTaxonomy: function (e) {
      e.preventDefault();
      this.showSuccessAlert = false;
      let formData = new FormData();
      formData.append('taxonomy', this.$refs.fileInput.files[0] || '');
      fetch(`/api/annualreports/${this.$route.params.id}/`, {
        method: "PATCH",
        headers: {'X-CSRFTOKEN': CSRF_TOKEN,},
        body: formData,
      }).then(response => {
        this.$emit('fetchData');
        this.$refs.fileInput.value = "";
        if(!response.ok)
          throw new Error(response.status);
        this.showSuccessAlert = true;
      }).catch((error => console.log(error)));
    },
  },
  computed: {
    currentTaxonomyName: function () {
      if (!this.report.taxonomy)
        return 'empty';
      return this.report.taxonomy.replace(/^.*[\\\/]/, '');
    },
  }
}
</script>

<style>

</style>
