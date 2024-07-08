import axios from 'axios';
import { SET_NAME, SET_MESSAGE, SET_ATTENDANCE } from './types';

export const setName = (name) => ({
  type: SET_NAME,
  payload: name,
});

export const setMessage = (message) => ({
  type: SET_MESSAGE,
  payload: message,
});

export const setAttendance = (attendance) => ({
  type: SET_ATTENDANCE,
  payload: attendance,
});

export const registerFace = (name) => async (dispatch) => {
  try {
    const response = await axios.get('http://localhost:5000/register', { params: { name } });
    dispatch(setMessage(response.data));
  } catch (error) {
    dispatch(setMessage('Error registering face'));
  }
};

export const markAttendance = () => async (dispatch) => {
  try {
    const response = await axios.get('http://localhost:5000/mark_attendance');
    dispatch(setMessage(response.data));
  } catch (error) {
    dispatch(setMessage('Error marking attendance'));
  }
};

export const fetchAttendance = () => async (dispatch) => {
  try {
    const response = await axios.get('http://localhost:5000/attendance');
    dispatch(setAttendance(response.data));
  } catch (error) {
    dispatch(setMessage('Error fetching attendance'));
  }
};
