import API from "@js/api";
import events from "@store/events";

export default {
  actions: {
    getProfileEvents({ state }) {
      const { events: eventsData } = events;
      return API.fetch("events/").then(({ data }) => {
        return data.map(event => {
          const extraData = eventsData.find(e => e.name === event.slug);
          return { ...event, ...extraData };
        });
      });
    },
    createEventTeam({ state }, { eventId, teamName }) {
      const body = {
        event: eventId,
        team_name: teamName
      };
      return API.post("teams/create/", { body });
    },
    joinEventTeam({ state }, { eventId, accessCode }) {
      const body = {
        access_code: accessCode
      };
      return API.post("teams/join/", { body });
    },
    removeMemberFromTeam({ state }, { teamId, memberId }) {
      const body = {
        member: memberId
      };
      return API.post(`teams/${teamId}/remove/`, { body });
    },
    leaveTeam({ state }, { teamId }) {
      return API.delete(`teams/${teamId}/`);
    }
  }
};
