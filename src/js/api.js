import Frisbee from "frisbee";

const api = new Frisbee({
  baseURI: "https://codefest-api.herokuapp.com",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json"
  }
});

export const STATUS = {
  NONE: "none",
  LOADING: "loading",
  SUCCESS: "success",
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

  static loading() {
    return new Response(null, STATUS.LOADING, null);
  }

  static clientError(err) {
    return new Response(null, STATUS.ERROR_UNKNOWN, err.message);
  }

  static responseError(response) {
    const { message } = response.err;
    switch (response.status) {
      case 401:
        return new Response(null, STATUS.ERROR_UNAUTHENTICATED, message);
      case 403:
        return new Response(null, STATUS.ERROR_FORBIDDEN, message);
      case 404:
        return new Response(null, STATUS.ERROR_NOT_FOUND, message);
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
  fetch(url, token) {
    return new Promise((resolve, reject) => {
      const options = {
        headers: {
          Authorization: `Token ${token}`
        }
      };
      resolve(Response.loading());
      api
        .get(url, options)
        .then(response => {
          if (response.status == STATUS.SUCCESS) resolve(response);
          else reject(response);
        })
        .catch(response => reject(response));
    });
  }
};
