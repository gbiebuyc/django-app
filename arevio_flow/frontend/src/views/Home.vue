<template>
  <div class="home">
    <div class="row" style=" display: flex; align-items: center;">
      <div class="col-6">
        <b-form-select
          v-model="selectedCompany"
          :options="userdata.companies"
          style="width: 250px"
          class="my-3"
          :disabled="userdata.companies.length < 2"
        ></b-form-select>
        <b-button-toolbar class="mb-3">
          <b-button class="mr-2" :disabled="selectedCompany === null" size="sm" v-b-modal.new-report>New report</b-button>
          <b-button class="mr-2" :disabled="selectedRows.length == 0" size="sm" v-b-modal.delete-confirm>Delete</b-button>
        </b-button-toolbar>
      </div>
      <div class="col-6" style="text-align: right">
        <img v-if="selectedCompany" id="company-logo" :src="selectedCompany.logo || 'data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4QAiRXhpZgAATU0AKgAAAAgAAQESAAMAAAABAAEAAAAAAAD/2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz/2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wAARCACvAPoDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9xKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKM0AFFGaM0AFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFF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b3Ze48O3X2STr9juWZ4m9lfll/4Fu+oFeP8AiXwlqfg2/wDsuqWU9lNzt8xflkA7qwyrD3UmvsCq2raPa69YSWt9a295ayfeimQOp98Hv79RVqfcnlPjjPFaHhnwjqnjTUDa6XZTXsy437B8kee7MflUf7xFe8j9l3wyNd+1f6f9k6/YfP8A3Wf97G/b7bs++OK7/StJtdCsI7WytreztYvuRQoEUfgO/v1NPmXQOU8p8B/srWtlsuPENx9tk6/ZLZysI9mfhm+i7R7kV61bW0dnbxwwxrHFCgREUYVFAwAB6AACpKKhu5QE4FeN/FP9nrXPG3xA1LVbO60eO2vDGUWeaRZBtiRDkLGR1U969kooTsB89/8ADJ/iT/n88P8A/gRN/wDGqQ/sn+JCP+P3w/8A+BE3/wAar6Fop8zFyo898dfAqHxx4O0e3eeOz1rSLKK1W4UFopAqAFG6EruBIOMjJ4OcV5m37OnjXTTLBbxwvDJw7QX6pHJ9QxUn8RX0dijFHOwseN/C/wDZjk0jV7fUPEE1tJ9lYSRWUBLqzDoZGwBgHnaM54ycZB7z4qeBNJ+IujrZ6hdR2d1CTLbXG5fMhJ4PBI3KccjjOByCAR1BHFecfHr4LTfEoWuoae0K6pZxmExynatxHksAG7MCWxng7jkjGaL3eodDhG/ZN1y4mXy9S0Ga1P3ZvMkyR0ztCEZ/4Fj3rnfjF4Dtfhtrun6XbztdTLYrNdTMNu+VpH6Lk7QFC4HPGCSSTW1oUPxO+H9j/Z2n2es29srErGlnHdRoScnaxVwMkk/KcZJPUmpPD3wC8UeP/ELXniDzrGGd99zcXMga4lHoiZJBxwN2AoHoMVoI9Q8JeDrTxl8C9H0vUY2aC40+FgV4eM43K6n1GQf0OQSD5hq/7MnifQ9Q36XNa36KSIpop/s0oHuGIwfoxH8q+gbW1jsraKGFFjhhRY40HRFUAAfgABUlZ81h2Pn7w7+y5r+sah5msXFtp8LNmZ/N+0XD+uAPlz2yW/A9K918PaDa+F9EtdPsY/JtbNPLjXOTjqST3JJJJ7kmrmKKJSuMKKKKkAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAxRiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKAP/9k='">
      </div>
    </div>

    <b-table ref="reportsTable"
      striped outlined hover
      :items="userdata.reports"
      :fields="fields"
      :filter="filter"
      :filter-included-fields="filterIncludedFields"
      selectable
      select-mode="multi"
      @row-selected="onRowSelected"
    > <template v-slot:cell(actions)="row">
        <b-button size="sm" class="mr-1" @click="onClickDownloadReport(row.item)" :disabled="row.item.downloading">
          <span v-if="row.item.downloading"><b-spinner small></b-spinner> Downloading...</span>
          <span v-else> Download</span>
        </b-button>
        <b-button size="sm" class="mr-1" @click="onClickUploadReport(row.item)"> Upload </b-button>
        <b-button size="sm" class="mr-1" v-b-modal.notyetimplemented> Preview </b-button>
      </template>
    </b-table>

    <b-modal id="new-report"
      centered
      title="Create a new report"
      @ok="newReport"
      @shown="initNewReportModal"
    > <p>Name:
      <b-form-input v-model="newReportName" ref="focusThis" placeholder="Enter the report name"></b-form-input></p>
      <p>Taxonomy:<br>
      <b-form-select
        v-model="newReportTaxonomy"
        :options="userdata.taxonomies"
        value-field="id"
        text-field="name"
        style="width: 250px"
      ></b-form-select></p>
    </b-modal>

    <b-modal id="delete-confirm" title="Delete?" @ok="onClickDeleteReport">
      {{ selectedRows.map(a => a.name).join(', ') }}
    </b-modal>

    <b-modal id='upload-spinner-modal'
      centered
      hide-footer
      hide-header
      size="sm"
    > <div class="text-center">
        <b-spinner></b-spinner>
      </div>
    </b-modal>

    <b-modal id='upload-done-modal'
      :title="'Import ' + (uploadLog && uploadLog.success ? 'success' : 'fail')"
      centered
      size="lg"
      ok-only
    > <h6>Arevio output:</h6>
      {{ uploadLog ? uploadLog.arevio_output : '' }}
    </b-modal>

    <b-form-file id="myFileInput"
      v-model="file"
      @input="onFileInput"
      class="d-none"
    ></b-form-file>

  </div>
</template>

<script>
import { CSRF_TOKEN } from "@/common/csrf_token.js"
import download from 'downloadjs'
export default {
  name: 'home',
  props: ['userdata'],
  computed: {
    filter: function () {
      try {
        return this.selectedCompany.id.toString();
      } catch (err) {
        return null;
      }
    },
  },
  data() {
    return {
      selectedCompany: this.userdata.companies[0].value,
      fields: [
        {
          key: 'name',
          sortable: true,
          formatter: value => value ? value : "No name",
        },
        {
          key: 'taxonomy',
          sortable: true,
          formatter: value => this.userdata.taxonomyNames[value],
        },
        {
          key: 'updated_at',
          sortable: true,
          formatter: value => new Date(value).toLocaleString(),
        },
        'actions',
      ],
      filterIncludedFields: ['company'],
      newReportName: null,
      newReportTaxonomy: this.userdata.taxonomies[0].id,
      selectedRows: [],
      file: null,
      uploadId: null,
      uploadLog: null,
    }
  },
  methods: {
    onRowSelected(items) {
      this.selectedRows = items;
    },
    newReport() {
      fetch('/annualreports/', {
        method: "POST",
        body: JSON.stringify({
          company: this.selectedCompany.id,
          taxonomy: this.newReportTaxonomy,
          name: this.newReportName,}),
        headers: {
          'X-CSRFTOKEN': CSRF_TOKEN,
          'Content-Type': 'application/json'},
        }).then(() => this.$emit('fetchData'))
    },
    onClickDeleteReport() {
      let rowsToDelete = [...this.selectedRows];
      rowsToDelete.forEach(row => {
        fetch(`/annualreports/${row.id}/`, {
          method: "DELETE",
          headers: {'X-CSRFTOKEN': CSRF_TOKEN},
        }).then(() => this.$emit('fetchData'))
      });
    },
    initNewReportModal() {
      this.$refs.focusThis.focus();
      this.newReportName = "";
    },
    onClickDownloadReport(item) {
      item.downloading = true;
      this.$refs.reportsTable.refresh()
      fetch(`/annualreports/${item.id}/`, {
          method: "GET",
          headers: {'X-CSRFTOKEN': CSRF_TOKEN},
        }).then(resp => {
          return resp.blob();
        }).then(blob => {
          download(blob, `${item.name}.xlsx`);
          item.downloading = false;
          this.$refs.reportsTable.refresh()
        });
    },
    onClickUploadReport(item) {
      this.file = null;
      this.uploadLog = null;
      this.uploadId = item.id;
      document.getElementById('myFileInput').click();
    },
    onFileInput(file) {
      if (file == null)
        return;
      this.$bvModal.show('upload-spinner-modal');
      let formData = new FormData();
      formData.append('excel_file', file);
      fetch(`/annualreports/${this.uploadId}/`, {
        method: 'POST',
        headers: {'X-CSRFTOKEN': CSRF_TOKEN,},
        body: formData,
      }).then(resp => {
        return resp.json();
      }).then(json => {
        this.uploadLog = json;
        this.$bvModal.hide('upload-spinner-modal');
        this.$bvModal.show('upload-done-modal');
        this.$emit('fetchData');
      });
    },
  },
  mounted() {
    this.$root.$on('bv::modal::hide', (bvEvent, modalId) => {
      if (modalId == 'upload-spinner-modal' && this.uploadLog == null) {
        bvEvent.preventDefault();
      }
    })
  }
};
</script>

<style scoped>
#company-logo {
    max-width: 150px;
    height: 75px;
    object-fit: contain;
}
#newReportButton {
  position: sticky;
  bottom: 30px;
  left: 100%;
}
</style>
