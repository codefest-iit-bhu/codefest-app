<template>
  <div :class="$style.root">
    <AppBar/>
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <div :class="$style.formContainer" slot="basic">
          <form :class="$style.form" @submit.prevent="submitForm">
            <div :class="$style.card" v-show="curId==null">
              <div :class="$style.loader"></div>
            </div>
            <div :class="$style.card" id="basic" v-show="curId=='basic'">
              <h3>basic</h3>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="name" :class="$style.label">name</label>
                  <input
                    type="text"
                    id="name"
                    v-model="profile.name"
                    :class="$style.field"
                    required
                  >
                </div>
                <div :class="$style.field">
                  <label for="gender" :class="$style.label">gender</label>
                  <select :class="$style.field" v-model="profile.gender" id="gender" required>
                    <option value="0">Male</option>
                    <option value="1">Female</option>
                    <option value="2">Others</option>
                  </select>
                </div>
                <div :class="$style.field">
                  <label for="phone" :class="$style.label">phone</label>
                  <input
                    type="phone"
                    id="phone"
                    :class="$style.field"
                    v-model="profile.phone"
                    required
                  >
                </div>
                <div :class="$style.field">
                  <label for="country" :class="$style.label">country</label>
                  <input
                    type="country"
                    id="country"
                    :class="$style.field"
                    v-model="profile.country"
                    required
                  >
                </div>
                <div :class="$style.field">
                  <label for="institute_type" :class="$style.label">you are a</label>
                  <select
                    :class="$style.field"
                    id="institute_type"
                    v-model="profile.institute_type"
                    required
                  >
                    <option value="0">School student</option>
                    <option value="1">College student</option>
                    <option value="2">Proffesional</option>
                  </select>
                </div>
                <div :class="$style.btnStyle">
                  <span @click="nav('academic')" :class="$style.next">
                    <i class="fas fa-arrow-circle-right"></i>
                  </span>
                </div>
              </div>
            </div>
            <div :class="$style.card" id="academic" v-show="curId=='academic'">
              <h3>academic</h3>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="institute_name" :class="$style.label">
                    <span v-if="profile.institute_type==2">last institute</span>
                    <span v-else>institute</span>
                  </label>
                  <input type="text" id="institute_name" v-model="profile.institute_name" required>
                </div>
                <div :class="$style.field">
                  <label for="study_year" :class="$style.label">
                    <span v-if="profile.institute_type==0">class</span>
                    <span v-if="profile.institute_type==1">year</span>
                    <span v-if="profile.institute_type==2">experience</span>
                  </label>
                  <input
                    type="number"
                    id="study_year"
                    name="study_year"
                    v-model="profile.study_year"
                  >
                </div>
                <div :class="$style.field" v-show="profile.institute_type==1">
                  <label for="branch" :class="$style.label">branch</label>
                  <input type="text" id="branch" name="branch" v-model="profile.branch">
                </div>
                <div :class="$style.field" v-show="profile.institute_type!=0">
                  <label for="degree" :class="$style.label">degree</label>
                  <input type="degree" id="degree" v-model="profile.degree">
                </div>
              </div>
              <div :class="$style.btnStyle">
                <span @click="nav('handles')" :class="$style.next">
                  <i class="fas fa-arrow-circle-right"></i>
                </span>
              </div>
            </div>
            <div :class="$style.card" id="handles" v-show="curId=='handles'">
              <h3>handles</h3>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="codeforces" :class="$style.label">codeforces</label>
                  <input type="text" v-model="handles.codeforces">
                </div>
                <div :class="$style.field">
                  <label for="codechef" :class="$style.label">codechef</label>
                  <input type="text" v-model="handles.codechef">
                </div>
                <div :class="$style.field">
                  <label for="hackerrank" :class="$style.label">hackerrank</label>
                  <input type="text" v-model="handles.hackerrank">
                </div>
                <div :class="$style.field">
                  <label for="hackerearth" :class="$style.label">hackerearth</label>
                  <input type="text" v-model="handles.hackerearth">
                </div>
                <div :class="$style.field">
                  <label for="topcoder" :class="$style.label">topcoder</label>
                  <input type="text" v-model="handles.topcoder">
                </div>
                <div :class="$style.field">
                  <label for="analyticsVidya" :class="$style.label">analytics vidya</label>
                  <input type="text" v-model="handles.analyticsVidya">
                </div>
                <div :class="$style.field">
                  <label for="dev_folio" :class="$style.label">dev folio</label>
                  <input type="text" v-model="handles.dev_folio">
                </div>
              </div>
              <div :class="$style.btnStyle">
                <button type="submit" name="submit" value=">" :class="$style.submit">Save</button>
              </div>
            </div>

            <div :class="$style.formNav">
              <i
                class="fas fa-circle"
                @click="nav('basic')"
                :class="curId=='basic'?$style.active:''"
              ></i>
              <i
                class="fas fa-circle"
                @click="nav('academic')"
                :class="curId=='academic'?$style.active:''"
              ></i>
              <i
                class="fas fa-circle"
                @click="nav('handles')"
                :class="curId=='handles'?$style.active:''"
              ></i>
            </div>
          </form>
          <datalist id="instituteList"></datalist>
          <datalist id="countryList"></datalist>
          <datalist id="branchList"></datalist>
        </div>
      </div>
    </main>
    <Footer/>
  </div>
</template>

    <script>
import AppBar from "@components/Menu/AppBar";
import Footer from "@components/Footer";
import TabLayout from "@components/layouts/TabLayout";
import firebase from "firebase";
import API from "@js/api";

export default {
  components: {
    AppBar,
    Footer,
    TabLayout
  },
  data() {
    return {
      profile: {},
      handles: {},
      curId: null,
      navIds: {
        basic: 0,
        academic: 1,
        handles: 2
      },
      isDisabled: {
        basic: false,
        academic: false,
        handles: false
      }
    };
  },
  methods: {
    checkValidity(fields) {
      if (fields == null) return true;
      var valid = true;
      fields.forEach(function(field) {
        if (!field.checkValidity()) {
          valid = false;
        }
      });
      return valid;
    },
    nav(id) {
      if (this.curId != null)
        var fields = document.querySelectorAll("#" + this.curId + " input");
      else var fields = null;
      if (
        this.checkValidity(fields) ||
        (this.curId == null || this.navIds[id] <= this.navIds[this.curId])
      ) {
        if (!this.isDisabled[id]) this.curId = id;
      } else document.querySelectorAll("form button")[0].click();
    },
    fillDropdown(dataUrl, dataDiv, dropdown) {
      var dataList = document.getElementById(dataDiv);
      var input = document.getElementById(dropdown);
      input.setAttribute("list", dataDiv);

      let url = dataUrl;

      var request = new XMLHttpRequest();

      request.onreadystatechange = function(response) {
        if (request.readyState === 4) {
          if (request.status === 200) {
            var jsonOptions = JSON.parse(request.responseText);

            jsonOptions.forEach(function(item) {
              var option = document.createElement("option");
              option.value = item.name;
              dataList.appendChild(option);
            });

            input.placeholder = "";
          } else {
            input.placeholder = "error";
          }
        }
      };

      input.placeholder = "";

      request.open("GET", url, true);
      request.send();
    },
    submitForm() {
      if (!this.profile.is_profile_complete) {
        API.put("profile/", {
          body: this.profile
        }).catch(console.log);
      }
      API.put("profile/handles/", {
        body: this.handles
      })
        .then(resp => {
          this.$router.push({ name: "~/dashboard" });
        })
        .catch(console.log);
    }
  },
  created() {
    API.fetch("profile/", { token: this.$store.getters.authToken })
      .then(({ data }) => {
        this.profile = data;
        if (!data.is_profile_complete) {
          this.nav("basic");
        } else {
          this.isDisabled["basic"] = true;
          this.isDisabled["academic"] = true;
          this.nav("handles");
        }
      })
      .catch(console.log);
    API.fetch("profile/handles/", { token: this.$store.getters.authToken })
      .then(({ data }) => {
        this.handles = data;
      })
      .catch(console.log);
  },
  mounted() {
    this.fillDropdown(
      "assets/institutes.json",
      "instituteList",
      "institute_name"
    );
    this.fillDropdown("assets/countries.json", "countryList", "country");
    this.fillDropdown("assets/branches.json", "branchList", "branch");
  }
};
</script>
    <style module lang="stylus">
    @require '~@styles/theme';
    @require '~@styles/anims';

    .authContainer {
      font-size: 16px;
      font-family: courier, monospace;
      max-width: 700px;
      margin: auto;
      width: 100%;
    }

    .wrapper {
      width: 80%;
      margin: 0 auto;
      padding: 100px 0;
      position: relative;
      top: 0;
      z-index: 1;
      font-family: 'Roboto Mono';
      font-size: 18px;
    }

    .root {
      height: 100%;
    }

    .form {
      margin: 20px;
      min-height: 400px;
      position: relative;
      border: 1px solid $chartreuse;
      border-radius: 4px 4px 0 0;
      box-shadow: inset 0px 0px 15px $chartreuse;

      .formNav {
        width: 100%;
        position: absolute;
        bottom: 0;
        text-align: center;
        border-top: 1px solid $chartreuse;
        padding: 20px;
        margin: 0;
        border-radius: 0 0 4px 4px;

        i {
          cursor: pointer;

          &.active {
            color: $chartreuse;
          }
        }
      }

      .card {
        padding: 20px;
        margin: 10px;
        width: 100%;
        min-height: 500px;
        position: relative;

        h3 {
          color: $chartreuse;
          text-align: center;
          text-transform: uppercase;
        }

        .loader {
          margin: auto;
          position: absolute;
          top: calc(50% - 60px);
          left: calc(50% - 30px);
          border: 5px solid $white;
          border-radius: 50%;
          border-top: 5px solid $chartreuse;
          width: 60px;
          height: 60px;
          -webkit-animation: spin 2s linear infinite; /* Safari */
          animation: spin 2s linear infinite;
        }

        @keyframes spin {
          0% {
            -webkit-transform: rotate(0deg);
          }

          100% {
            -webkit-transform: rotate(360deg);
          }
        }

        @keyframes spin {
          0% {
            transform: rotate(0deg);
          }

          100% {
            transform: rotate(360deg);
          }
        }

        .fieldsContainer {
          width: 100%;
          margin-bottom: 15px;
          text-align: right;
        }

        .field {
          input, select {
            height: 30px;
            color: white;
            border: 0;
            outline: 0;
            max-width: 400px;
            width: 100%;
            font-size: 16px;
            background: #fff2;
            border-radius: 5px;
            padding-left: 5px;
            margin-bottom: 15px;
          }

          option {
            color: black;
          }

          .label {
            float: left;
            clear: both;
            color: white;
            text-align: right;
            height: 30px;
            margin-bottom: 15px;
          }
        }

        .btnStyle {
          text-align: center;

          .submit {
            border-radius: 4px;
            background: $chartreuse;
            color: black;
            border: 1px solid $limeade;
            height: 30px;
            width: 70px;
            cursor: pointer;
            text-align: center;

            &:hover {
              background: $limeade;
              color: $white;
            }
          }

          .next {
            border: 0;
            background: transparent;
            color: $white;
            border-radius: 100%;
            font-size: 30px;
            height: 30px;
            width: 30px;
            cursor: pointer;
            text-align: center;

            &:hover {
              color: $chartreuse;
            }
          }
        }

        .social {
          width: 100%;
          max-width: 600px;
          margin: auto;
          text-align: center;
          padding: 5px;
          margin-top: 20px;
          border: 0;
          border-top: 1px solid $chartreuse;

          .socialButton {
            background-color: Transparent;
            background-repeat: no-repeat;
            border: none;
            cursor: pointer;
            overflow: hidden;
            outline: none;

            img {
              margin: 10px;
              width: 40px;
              height: 40px;
            }
          }
        }
      }
    }

    @media screen and (max-width: 769px) {
      .wrapper {
        width: 90%;
      }
    }
</style>
