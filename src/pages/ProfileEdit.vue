<template>
  <div :class="[$style.root, $style[$mq]]">
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
                    type="tel"
                    pattern="\+[0-9]{9,15}"
                    placeholder="(e.g. +910000000000)"
                    id="phone"
                    :class="$style.field"
                    v-model="profile.phone"
                    required
                  >
                </div>
                <div :class="$style.field">
                  <label for="country" :class="$style.label">country</label>
                  <select id="country" :class="$style.field" v-model="profile.country" required>
                    <option selected disabled>Select your country</option>
                  </select>
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
                    <option value="2">Professional</option>
                  </select>
                </div>
                <div :class="$style.btnStyle">
                  <button type="button" @click="nav('academic')" :class="$style.next">
                    <i class="fas fa-arrow-circle-right"></i>
                  </button>
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
                  <input
                    type="text"
                    id="institute_name"
                    placeholder="Type out your institute"
                    v-model="profile.institute_name"
                    required
                  >
                </div>
                <div :class="$style.field">
                  <label for="study_year" :class="$style.label">
                    <span v-if="profile.institute_type==0">class</span>
                    <span v-if="profile.institute_type==1">study year</span>
                    <span v-if="profile.institute_type==2">experience</span>
                  </label>
                  <input
                    type="number"
                    id="study_year"
                    name="study_year"
                    placeholder="(e.g. 2)"
                    min="1"
                    v-model="profile.study_year"
                    required
                  >
                </div>
                <div :class="$style.field" v-show="profile.institute_type==1">
                  <label for="branch" :class="$style.label">branch</label>
                  <input
                    type="text"
                    id="branch"
                    name="branch"
                    placeholder="Type out your branch"
                    v-model="profile.branch"
                  >
                </div>
                <div :class="$style.field" v-show="profile.institute_type!=0">
                  <label for="degree" :class="$style.label">degree</label>
                  <input type="degree" id="degree" v-model="profile.degree">
                </div>
              </div>
              <div :class="$style.btnStyle">
                <button type="button" @click="nav('handles')" :class="$style.next">
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </div>
            </div>
            <div :class="$style.card" id="handles" v-show="curId=='handles'">
              <h3>handles</h3>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="codeforces" :class="$style.label">codeforces</label>
                  <input type="text" @keyup="checkHandlesChanged" v-model="handles.codeforces">
                </div>
                <div :class="$style.field">
                  <label for="codechef" :class="$style.label">codechef</label>
                  <input type="text" @keyup="checkHandlesChanged" v-model="handles.codechef">
                </div>
                <div :class="$style.field">
                  <label for="hackerrank" :class="$style.label">hackerrank</label>
                  <input type="text" @keyup="checkHandlesChanged" v-model="handles.hackerrank">
                </div>
                <div :class="$style.field">
                  <label for="hackerearth" :class="$style.label">hackerearth</label>
                  <input type="text" @keyup="checkHandlesChanged" v-model="handles.hackerearth">
                </div>
                <div :class="$style.field">
                  <label for="topcoder" :class="$style.label">topcoder</label>
                  <input type="text" @keyup="checkHandlesChanged" v-model="handles.topcoder">
                </div>
                <div :class="$style.field">
                  <label for="analyticsVidya" :class="$style.label">analytics vidya</label>
                  <input type="text" @keyup="checkHandlesChanged" v-model="handles.analyticsVidya">
                </div>
                <div :class="$style.field">
                  <label for="dev_folio" :class="$style.label">dev folio</label>
                  <input type="text" @keyup="checkHandlesChanged" v-model="handles.dev_folio">
                </div>
              </div>
              <div :class="$style.btnStyle">
                <button type="submit" name="submit" :class="$style.submit">
                  <span v-if="isHandlesFilled">Save</span>
                  <span v-else>Skip</span>
                </button>
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
const AppBar = () => import("@components/Menu/AppBar");
const Footer = () => import("@components/Footer");
const TabLayout = () => import("@components/layouts/TabLayout");
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
      },
      isHandlesFilled: false
    };
  },
  methods: {
    checkHandlesChanged(event) {
      if (event.target.value.length > 0) this.isHandlesFilled = true;
    },
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
        // if (!this.isDisabled[id])
        this.curId = id;
      } else document.querySelectorAll("form button[type='submit']")[0].click();
    },
    fillDropdown(
      dataUrl,
      dataDiv,
      dropdown,
      valuefield = "name",
      datafield = "name"
    ) {
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
              option.value = item[valuefield];
              option.innerHTML = item[datafield];
              dataList.appendChild(option);
            });
          } else {
            console.log("error");
          }
        }
      };

      request.open("GET", url, true);
      request.send();
    },
    submitForm() {
      API.put("profile/handles/", {
        body: this.handles
      })
        .then(resp => {
          API.put("profile/", {
            body: this.profile
          })
            .then(_ => {
              const msg = "Your profile has been updated successfully!";
              this.$toasted.global.success({ message: msg });
              this.$router.push({ name: "~/dashboard" });
            })
            .catch(err => {
              this.$toasted.global.error_post({ message: err.message });
            });
        })
        .catch(err => {
          this.$toasted.global.error_post({ message: err.message });
        });
    }
  },
  created() {
    API.fetch("profile/")
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
    API.fetch("profile/handles/")
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
    this.fillDropdown("assets/branches.json", "branchList", "branch");
    this.fillDropdown(
      "assets/countries.json",
      "country",
      "country",
      "code",
      "name"
    );
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
  margin: 50px auto;
  width: 100%;
}

.wrapper {
  width: 100%;
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
  position: relative;
  border: 1px solid $chartreuse;
  border-radius: 5px;
  box-shadow: inset 0px 0px 15px $chartreuse;
  background: #111;

  .formNav {
    width: 100%;
    text-align: center;
    border-top: 1px solid $chartreuse;
    padding: 20px;
    margin: 0;

    i {
      cursor: pointer;

      &.active {
        color: $chartreuse;
      }
    }
  }

  .card {
    padding: 10px 20px;
    min-height: 400px;
    margin: 5px;
    width: 100%;
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
      padding: 5px;
      margin: 5px auto;
      text-align: right;
    }

    .field {
      margin: 10px auto;
      margin-top: 20px;
      text-align: center;

      input, select {
        text-align: left;
        display: inline-block;
        height: 30px;
        width: calc(100% - 120px);
        color: white;
        border: 0;
        outline: 0;
        margin: auto;
        font-size: 16px;
        border-radius: 5px;
        padding-left: 5px;
        background: #fff2;
      }

      .fieldWrapper {
        width: 100%;
        position: relative;

        i {
          top: 0;
          right: 7px;
          position: absolute;
          cursor: pointer;
        }
      }

      option {
        color: black;
      }

      .label {
        display: inline-block;
        text-align: left;
        text-transform: capitalize;
        width: 100px;
        color: white;
        height: 30px;
      }
    }

    .btnStyle {
      text-align: center;

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

      .submit {
        border-radius: 4px;
        width: 80px;
        padding: 5px 10px;
        font: 14pt Ubuntu;
        background: transparent;
        color: $white;
        text-transform: uppercase;
        border: 1px solid $white;

        &:hover {
          border: 1px solid $chartreuse;
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

.xs, .sm {
  .form {
    .field {
      input, select, .label {
        font-size: 16px;
        width: 100%;
      }
    }
  }
}
</style>
