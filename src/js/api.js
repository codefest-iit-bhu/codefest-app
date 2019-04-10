import Frisbee from "frisbee";

export default new Frisbee({
  baseURI: "https://codefest-api.herokuapp.com",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json"
  }
});
