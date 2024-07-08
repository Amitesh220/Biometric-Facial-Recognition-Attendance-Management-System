import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';
import { composeWithDevTools } from 'redux-devtools-extension'; // For Redux DevTools
import attendanceReducer from './reducers/attendanceReducer'; // Example reducer

const rootReducer = combineReducers({
  // Add your reducers here
  attendance: attendanceReducer, // Example reducer
});

const store = createStore(
  rootReducer,
  composeWithDevTools(applyMiddleware(thunk))
);

export default store;
