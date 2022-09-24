<template>
  <div :class="[$style.root, $style[$mq]]">
    <AppBar />
    <main :class="$style.wrapper">
      <div :class="$style.authContainer">
        <div :class="$style.formContainer" slot="basic">
          <form :class="$style.form" @submit.prevent="submitForm">
            <div :class="$style.card" v-show="curId == null">
              <div :class="$style.loader"></div>
            </div>
            <div :class="$style.card" id="basic" v-show="curId == 'basic'">
              <h2>Basic</h2>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="name" :class="$style.label">Name</label>
                  <input
                    type="text"
                    id="name"
                    v-model="profile.name"
                    :class="$style.field"
                    required
                  />
                </div>
                <div :class="$style.field">
                  <label for="gender" :class="$style.label">Gender</label>
                  <select
                    :class="$style.field"
                    v-model="profile.gender"
                    id="gender"
                    required
                  >
                    <option value="0">Male</option>
                    <option value="1">Female</option>
                    <option value="2">Others</option>
                  </select>
                </div>
                <div :class="$style.field">
                  <label for="phone" :class="$style.label">Phone</label>
                  <input
                    type="tel"
                    pattern="\+[0-9]{9,15}"
                    placeholder="(e.g. +910000000000)"
                    id="phone"
                    :class="$style.field"
                    v-model="profile.phone"
                    required
                  />
                </div>
                <div :class="$style.field">
                  <label for="country" :class="$style.label">Country</label>
                  <select
                    id="country"
                    :class="$style.field"
                    v-model="profile.country"
                    required
                  >
                    <option selected disabled>Select your country</option>
                  </select>
                </div>
                <div :class="$style.field">
                  <label for="institute_type" :class="$style.label"
                    >You are a</label
                  >
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
                  <button
                    type="button"
                    @click="nav('academic')"
                    :class="$style.next"
                  >
                    <i class="fas fa-arrow-circle-right"></i>
                  </button>
                </div>
              </div>
            </div>
            <div
              :class="$style.card"
              id="academic"
              v-show="curId == 'academic'"
            >
              <h2>Academic</h2>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="institute_name" :class="$style.label">
                    <span v-if="profile.institute_type == 2"
                      >Last Institute</span
                    >
                    <span v-else>Institute</span>
                  </label>
                  <input
                    type="text"
                    id="institute_name"
                    placeholder="Type out your institute"
                    v-model="profile.institute_name"
                    required
                  />
                </div>
                <div :class="$style.field">
                  <label for="study_year" :class="$style.label">
                    <span v-if="profile.institute_type == 0">class</span>
                    <span v-if="profile.institute_type == 1">Study Year</span>
                    <span v-if="profile.institute_type == 2">experience</span>
                  </label>
                  <input
                    type="number"
                    id="study_year"
                    name="study_year"
                    placeholder="(e.g. 2)"
                    min="1"
                    v-model="profile.study_year"
                    required
                  />
                </div>
                <div :class="$style.field" v-show="profile.institute_type == 1">
                  <label for="branch" :class="$style.label">Branch</label>
                  <input
                    type="text"
                    id="branch"
                    name="branch"
                    placeholder="Type out your branch"
                    v-model="profile.branch"
                  />
                </div>
                <div :class="$style.field" v-show="profile.institute_type != 0">
                  <label for="degree" :class="$style.label">Degree</label>
                  <input type="degree" id="degree" v-model="profile.degree" />
                </div>
              </div>
              <div :class="$style.btnStyle">
                <button
                  type="button"
                  @click="nav('handles')"
                  :class="$style.next"
                >
                  <i class="fas fa-arrow-circle-right"></i>
                </button>
              </div>
            </div>
            <div :class="$style.card" id="handles" v-show="curId == 'handles'">
              <h2>Handles</h2>
              <div :class="$style.fieldsContainer">
                <div :class="$style.field">
                  <label for="codeforces" :class="$style.label"
                    >Codeforces</label
                  >
                  <input
                    type="text"
                    @keyup="checkHandlesChanged"
                    v-model="handles.codeforces"
                  />
                </div>
                <div :class="$style.field">
                  <label for="codechef" :class="$style.label">Codechef</label>
                  <input
                    type="text"
                    @keyup="checkHandlesChanged"
                    v-model="handles.codechef"
                  />
                </div>
                <div :class="$style.field">
                  <label for="hackerrank" :class="$style.label"
                    >Hackerrank</label
                  >
                  <input
                    type="text"
                    @keyup="checkHandlesChanged"
                    v-model="handles.hackerrank"
                  />
                </div>
                <div :class="$style.field">
                  <label for="hackerearth" :class="$style.label"
                    >Hackerearth</label
                  >
                  <input
                    type="text"
                    @keyup="checkHandlesChanged"
                    v-model="handles.hackerearth"
                  />
                </div>
                <div :class="$style.field">
                  <label for="topcoder" :class="$style.label">Topcoder</label>
                  <input
                    type="text"
                    @keyup="checkHandlesChanged"
                    v-model="handles.topcoder"
                  />
                </div>
                <div :class="$style.field">
                  <label for="analyticsVidya" :class="$style.label"
                    >Analytics Vidya</label
                  >
                  <input
                    type="text"
                    @keyup="checkHandlesChanged"
                    v-model="handles.analyticsVidya"
                  />
                </div>
                <div :class="$style.field">
                  <label for="dev_folio" :class="$style.label">Dev Folio</label>
                  <input
                    type="text"
                    @keyup="checkHandlesChanged"
                    v-model="handles.dev_folio"
                  />
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
                :class="curId == 'basic' ? $style.active : ''"
              ></i>
              <i
                class="fas fa-circle"
                @click="nav('academic')"
                :class="curId == 'academic' ? $style.active : ''"
              ></i>
              <i
                class="fas fa-circle"
                @click="nav('handles')"
                :class="curId == 'handles' ? $style.active : ''"
              ></i>
            </div>
          </form>
          <datalist id="instituteList"></datalist>
          <datalist id="countryList"></datalist>
          <datalist id="branchList"></datalist>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script>
import API from "@js/api";

const AppBar = () => import("@components/Menu/AppBar");
const Footer = () => import("@components/Footer");
const TabLayout = () => import("@components/layouts/TabLayout");

export default {
  components: {
    AppBar,
    Footer,
    TabLayout,
  },
  data() {
    return {
      profile: {},
      handles: {},
      curId: null,
      navIds: {
        basic: 0,
        academic: 1,
        handles: 2,
      },
      isDisabled: {
        basic: false,
        academic: false,
        handles: false,
      },
      isHandlesFilled: false,
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
        var fields = document.querySelectorAll(
          `#${this.curId} input, #${this.curId} select`
        );
      else var fields = null;
      if (
        this.checkValidity(fields) ||
        this.curId == null ||
        this.navIds[id] <= this.navIds[this.curId]
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
        body: this.handles,
      })
        .then((resp) => {
          API.put("profile/", {
            body: this.profile,
          })
            .then((_) => {
              const msg = "Your profile has been updated successfully!";
              this.$toasted.global.success({ message: msg });
              this.$router.push({ name: "~/dashboard" });
            })
            .catch((err) => {
              this.$toasted.global.error_post({ message: err.message });
            });
        })
        .catch((err) => {
          this.$toasted.global.error_post({ message: err.message });
        });
    },
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
  },
};
</script>
<style module lang="stylus">

@require '~@styles/anims';

.authContainer {
  $font-size: 16px;
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
  $font-size: 18px;
}

.root {
  height: 100%;
}

.form {
  margin: 20px;
  position: relative;
  border-radius: 0 40px;
  background-color: var(--background-color);
  box-shadow: var(--inset-box-shadow);

  .formNav {
    width: 100%;
    text-align: center;
    padding: 20px;
    margin: 0;

    i {
      cursor: pointer;

      &.active {
        color: $waterloo;
      }
    }
  }

  .card {
    padding: 10px 20px;
    min-height: 400px;
    margin: 5px;
    width: 100%;
    position: relative;

    h2 {
      color: var(--text-color);
      text-align: center;
      font-family: 'Roboto Slab';
    }

    .loader {
      margin: auto;
      position: absolute;
      top: calc(50% - 60px);
      left: calc(50% - 30px);
      border: 5px solid $white;
      border-radius: 50%;
      border-top: 5px solid $waterloo;
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
        color: var(--text-color);
        box-shadow: var(--inset-box-shadow);
        background-color: var(--background-color);
        width: calc(100% - 120px);
        border: 0;
        outline: 0;
        margin: auto;
        $font-size: 16px;
        border-radius: 5px;
        padding-left: 5px;
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
        width: 100px;
        color: var(--text-color);
        font-family: 'Quicksand';
        font-weight: 600;
        height: 30px;
      }
    }

    .btnStyle {
      text-align: center;

      .next {
        border: 0;
        background: transparent;
        color: var(--background-color-invert);
        box-shadow: var(--small-icon-shadow);
        border-radius: 100%;
        $font-size: 30px;
        height: 30px;
        width: 30px;
        cursor: pointer;
        text-align: center;

        &:hover {
          color: $waterloo;
        }
      }

      .submit {
        border-radius: 10px 0;
        border: none;
        width: 100px;
        padding: 10px 20px;
        font: 14pt Roboto Slab;
        font-weight: 600;
        background: var(--background-color);
        color: $waterloo;
        box-shadow: var(--small-icon-shadow);

        &:hover {
          color: var(--text-color);
          box-shadow: var(--inset-box-shadow);
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
        $font-size: 16px;
        width: 100%;
      }
    }
  }
}
</style>
