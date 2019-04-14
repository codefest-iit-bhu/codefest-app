import Frisbee from "frisbee";
import { MakeQuerablePromise } from "@js/utils";
import store from "@store";

const api = new Frisbee({
  baseURI: "https://codefest-api.herokuapp.com",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json"
  }
});

const getApiOptions = function({ body }) {
  const options = {};
  const token = store.getters.authToken;
  if (token) {
    options["headers"] = {
      Authorization: `Token ${token}`
    };
  }
  if (body) options["body"] = body;
  return options;
};

const apiWrapper = function(promise) {
  return MakeQuerablePromise(
    new Promise((resolve, reject) => {
      promise
        .then(response => {
          if (response.status == STATUS.ERROR_UNAUTHENTICATED)
            store.dispatch("logout");
          if (response.status == STATUS.SUCCESS) resolve(response);
          else reject(response);
        })
        .catch(reject);
    })
  );
};

export const STATUS = {
  NONE: "none",
  SUCCESS: "success",
  ERROR_BAD_REQUEST: "error.bad_request",
  ERROR_NOT_FOUND: "error.not_found",
  ERROR_UNAUTHENTICATED: "error.unauthenticated",
  ERROR_FORBIDDEN: "error.unauthorized",
  ERROR_UNKNOWN: "error.unknown"
};

export class Response extends Object {
  constructor(data, status, message) {
    super(arguments);
    this.data = data;
    this.status = status;
    this.message = message;
  }

  static success(data) {
    return new Response(data, STATUS.SUCCESS, null);
  }

  static clientError(err) {
    return new Response(null, STATUS.ERROR_UNKNOWN, err.message);
  }

  static responseError(response) {
    const { message } = response.err;
    switch (response.status) {
      case 400:
        return new Response(null, STATUS.ERROR_BAD_REQUEST, message);
      case 401:
        return new Response(null, STATUS.ERROR_UNAUTHENTICATED, message);
      case 403:
        return new Response(null, STATUS.ERROR_FORBIDDEN, message);
      case 404:
        return new Response(null, STATUS.ERROR_NOT_FOUND, message);
      default:
        return new Response(null, STATUS.ERROR_UNKNOWN, message);
    }
  }

  static handleResponse(response) {
    if (response.status >= 400) return Response.responseError(response);
    else if (response.status >= 200) return Response.success(response.body);
  }
}

api.interceptor.register({
  requestError: function(err) {
    return Response.clientError(err);
  },
  response: function(response) {
    return Response.handleResponse(response);
  },
  responseError: function(err) {
    return Response.clientError(err);
  }
});

export default {
  fetch(url, options = {}) {
    return apiWrapper(api.get(url, getApiOptions(options)));
  },
  post(url, options = {}) {
    return apiWrapper(api.post(url, getApiOptions(options)));
  },
  put(url, options = {}) {
    return apiWrapper(api.put(url, getApiOptions(options)));
  },
  delete(url, options = {}) {
    return apiWrapper(api.delete(url, getApiOptions(options)));
  }
};
