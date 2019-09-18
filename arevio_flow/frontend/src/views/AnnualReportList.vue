<template>
  <div>
    <p v-if="loading">Loading...</p>
    <div v-else>
      <h1>Reports for {{ companyName }}</h1>
      <div id="NewReportLinkBox" style="display:block; text-align:left;">
        <a title="Add new report to the list" class="icon add" href="" onclick="return false;" @click="onClickAddReport">
          <span>[New Report]</span>
        </a>
      </div>

      <table>
        <thead>
          <tr class="header" id="theader">
            <th onclick="javascript:sortTable(0);">Name</th>
            <!-- <th class="detailsColumn" onclick="javascript:sortTable(1);"> -->
            <th class="detailsColumn">
              Taxonomy
            </th>
            <!-- <th class="detailsColumn" onclick="javascript:sortTable(2);"> -->
            <th class="detailsColumn">
              Date Modified
            </th>
            <th class="detailsColumn">
              Modified
            </th>
          </tr>
        </thead>
        <tbody id="tbody">
          <tr v-for="item in list" :key="item.id">
            <td><router-link title="Edit this report" class="icon file" to="/annualreport">{{ "Report_" + item.id.toString().padStart(3, 0) }}</router-link></td>
            <!-- <td><router-link class="icon file" to="/annualreport">Report</router-link></td> -->
            <td class="detailsColumn">{{ getFileNameFromPath(item.taxonomy) }}</td>
            <td class="detailsColumn">{{ new Date(item.updated_at).toLocaleString() }}</td>
            <td class="detailsColumn">{{ timeSince(new Date(item.updated_at)) + " ago" }}</td>
            <td>&nbsp;<a title="Delete this report" class="icon delete" href="" onclick="return false;" @click="onClickDeleteReport(item.id)"></a></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
export default {
  name: 'annualreportlist',
  data() {
    return {
      list: null,
      companyId: null,
      companyName: null,
    };
  },
  created() {
    this.companyId = this.$route.query.company;
    apiService(`/api/companies/${this.companyId}/`)
      .then(data => {
        this.companyName = data.name;
      })
    this.fetchData();
  },
  methods: {
    fetchData: function () {
      apiService(`/api/annualreports/?company=${this.companyId}`)
        .then(data => {
          this.list = data.results;
        })
    },
    timeSince: function (date) {
      var seconds = Math.floor((new Date() - date) / 1000);
      var interval = Math.floor(seconds / 31536000);
      if (interval > 1)
        return interval + " years";
      interval = Math.floor(seconds / 2592000);
      if (interval > 1)
        return interval + " months";
      interval = Math.floor(seconds / 86400);
      if (interval > 1)
        return interval + " days";
      interval = Math.floor(seconds / 3600);
      if (interval > 1)
        return interval + " hours";
      interval = Math.floor(seconds / 60);
      if (interval > 1)
        return interval + " minutes";
      return Math.floor(seconds) + " seconds";
    },
    getFileNameFromPath: function (path) {
      if (!path)
        return 'null';
      // eslint-disable-next-line
      return path.replace(/^.*[\\\/]/, '');
    },
    onClickAddReport: function() {
      apiService('/api/annualreports/', "POST", {"company": this.companyId})
        .then(() => this.fetchData());
    },
    onClickDeleteReport: function(reportId) {
      apiService(`/api/annualreports/${reportId}/`, "DELETE")
        .then(() => this.fetchData());
    },
  },
  computed: {
    loading: function () {
      return ((this.companyName === null) || (this.list === null)) ? true : false;
    },
  },
};
</script>

<style scoped>

  #main {
    padding: 30px;
  }

  /* th {
    cursor: pointer;
  } */

  td.detailsColumn {
    -webkit-padding-start: 2em;
    text-align: end;
    white-space: nowrap;
  }

  a.icon {
    -webkit-padding-start: 1.5em;
    text-decoration: none;
  }

  a.icon:hover {
    text-decoration: underline;
  }

  a.file {
    background : url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAAABnRSTlMAAAAAAABupgeRAAABHUlEQVR42o2RMW7DIBiF3498iHRJD5JKHurL+CRVBp+i2T16tTynF2gO0KSb5ZrBBl4HHDBuK/WXACH4eO9/CAAAbdvijzLGNE1TVZXfZuHg6XCAQESAZXbOKaXO57eiKG6ft9PrKQIkCQqFoIiQFBGlFIB5nvM8t9aOX2Nd18oDzjnPgCDpn/BH4zh2XZdlWVmWiUK4IgCBoFMUz9eP6zRN75cLgEQhcmTQIbl72O0f9865qLAAsURAAgKBJKEtgLXWvyjLuFsThCSstb8rBCaAQhDYWgIZ7myM+TUBjDHrHlZcbMYYk34cN0YSLcgS+wL0fe9TXDMbY33fR2AYBvyQ8L0Gk8MwREBrTfKe4TpTzwhArXWi8HI84h/1DfwI5mhxJamFAAAAAElFTkSuQmCC ") left top no-repeat;
  }

  a.dir {
    background : url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAd5JREFUeNqMU79rFUEQ/vbuodFEEkzAImBpkUabFP4ldpaJhZXYm/RiZWsv/hkWFglBUyTIgyAIIfgIRjHv3r39MePM7N3LcbxAFvZ2b2bn22/mm3XMjF+HL3YW7q28YSIw8mBKoBihhhgCsoORot9d3/ywg3YowMXwNde/PzGnk2vn6PitrT+/PGeNaecg4+qNY3D43vy16A5wDDd4Aqg/ngmrjl/GoN0U5V1QquHQG3q+TPDVhVwyBffcmQGJmSVfyZk7R3SngI4JKfwDJ2+05zIg8gbiereTZRHhJ5KCMOwDFLjhoBTn2g0ghagfKeIYJDPFyibJVBtTREwq60SpYvh5++PpwatHsxSm9QRLSQpEVSd7/TYJUb49TX7gztpjjEffnoVw66+Ytovs14Yp7HaKmUXeX9rKUoMoLNW3srqI5fWn8JejrVkK0QcrkFLOgS39yoKUQe292WJ1guUHG8K2o8K00oO1BTvXoW4yasclUTgZYJY9aFNfAThX5CZRmczAV52oAPoupHhWRIUUAOoyUIlYVaAa/VbLbyiZUiyFbjQFNwiZQSGl4IDy9sO5Wrty0QLKhdZPxmgGcDo8ejn+c/6eiK9poz15Kw7Dr/vN/z6W7q++091/AQYA5mZ8GYJ9K0AAAAAASUVORK5CYII= ") left top no-repeat;
  }

  a.add {
    background : url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAACIElEQVR4XqWTT0hUURjFf3f+aL6F5SpdFCS0KQhiaBkUTVY6YpugRbYJoiCoRfQHWgRBTjnVmMoUCZGLpBHXIUaFBekwpSAERdqmmhpnjJkyNWfe1/uQecjbuOjAd9+557vncO977xoR4b/gDWiOEWq6wUi4A9nnlD6duRzqZCRyi5DX62MVDt6kd71Vmz4XOR/uO/OQxKm7XD9+mbOt7ezetiNcFfCnIzGSeFIq5uSJvgZZkGcy/qVdEq+Q+Auk6yVy7zXSn2qUxOhOOdLtF2cnva5Xh5YYoaM9lvxYHJKByXrpcQzxUaSCLifs/hvkwVhQOp7Wy+E40nqbkHuE5RKdkV1tTH3rI7/wHfxgG1yUtQyIf5kaa476OrDLxAACKGDvlo2bmMoOULLBFliycaGcEgQFJ+AvtRZg2OO+g/1R5Pn0Semf3CBrIfEWuTSENHci7hGMgcL8LCbgY034vFMdDOSLGebLc3S/M9xJG6JjhgqUq9YzYfAbsG0wZlVAeYnUp8wMsljHumqocaq6ChfKVdNesQC//hhKi6TcgNx7oh++ZsnN2ojtIxCAYAAXylUrlyCbNWR+ClnH4wZMDDBczDE4MV1g5iMU8lAVhCefG7SUq+b0DNMZ4beufcyw9y5sbrrKiP4kpx8ZuZBELg6ulHLVtBe+QlLXul7PZWrc3saxA9cYb4npp1op5appr2L2BqyGBWwFQp5SzfLeo3+3Dz8xOncgCQAAAABJRU5ErkJggg==') left top no-repeat;
  }

  a.delete {
    background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABWUlEQVR4XqWSsS8EQRjF3665+AcUKoVWc+suNFcgQkEkJ1GKf0B3hUIiQiKh1MgVNEqdUBCFxFbshUKjoFCJXCIRwuVOPvuGb+3GyBVe8m1m5vfet5OZgYhAFQ7lhQWHXJxZPw37VzfASpvacV9hsLiMp7WKLY7V1I4bqN7f4JscqOfNFQSVBYRYp4ljrpEnXpWeQYEdX/Z25LE8qMW5c41eZpjVBkmT190tqc+UnEWmYf25wY9qpdOrYohqFMzOoXGyj7Q6R6dwuV0FPfQqMEhJgddo6HmouJbxqMyvqypP4+PiDB3ZBnaNLAQk3oWnIPMOCpMTkOsafGNsmb48S+eW0ZO+YqPh4vgY5PYm2brX04vo4BCUZfd3sIo9nHMntJlkK80mJPcd7urG+dGxHhjN0cDIMKT+8MVjr/MdtJbmWZmrotzc/Q5c4T+5NsiY3GE3Z9bj5z/6BNd0A44tKdxZAAAAAElFTkSuQmCC') left top no-repeat;
  }

  html[dir=rtl] a {
    background-position-x: right;
  }

  #NewReportLinkBox {
    margin-bottom: 10px;
    padding-bottom: 10px;
  }

  #listingParsingErrorBox {
    border: 1px solid black;
    background: #fae691;
    padding: 10px;
    display: none;
  }

  #tbody > tr > td:last-child > a {
    visibility: hidden;
    background-position: center;
  }

  #tbody > tr:hover > td:last-child > a {
    visibility: visible;
  }
</style>
