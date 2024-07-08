import { combineReducers } from 'redux';
import { SET_NAME, SET_MESSAGE, SET_ATTENDANCE } from '../actions/types';

const initialState = {
  name: '',
  message: '',
  attendance: [],
};

const appReducer = (state = initialState, action) => {
  switch (action.type) {
    case SET_NAME:
      return {
        ...state,
        name: action.payload,
      };
    case SET_MESSAGE:
      return {
        ...state,
        message: action.payload,
      };
    case SET_ATTENDANCE:
      return {
        ...state,
        attendance: action.payload,
      };
    default:
      return state;
  }
};

export default combineReducers({
  app: appReducer,
});
