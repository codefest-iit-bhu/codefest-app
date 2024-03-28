let KEY_AUTH_TOKEN = "auth-token";
let SITE_URL = "https://codefest.iitbhu.tech";
let KEY_THEME = "theme";
let BACKEND_URL = "https://codefest.iitbhu.tech/api";

try{
    const envSecrets = require("./env");
    KEY_AUTH_TOKEN = envSecrets.KEY_AUTH_TOKEN || KEY_AUTH_TOKEN
    SITE_URL = envSecrets.SITE_URL || SITE_URL
    KEY_THEME = envSecrets.KEY_THEME || KEY_THEME
    BACKEND_URL = envSecrets.BACKEND_URL || BACKEND_URL
}
catch(e){}

export {KEY_AUTH_TOKEN, SITE_URL, KEY_THEME, BACKEND_URL};
