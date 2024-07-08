import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { setName, setMessage, setAttendance, registerFace, markAttendance, fetchAttendance } from './actions';
import RegisterFaceForm from './components/RegisterFaceForm';
import './App.css';

function App() {
  const dispatch = useDispatch();
  const name = useSelector(state => state.app.name);
  const message = useSelector(state => state.app.message);
  const attendance = useSelector(state => state.app.attendance);

  const handleRegister = () => {
    dispatch(registerFace(name));
  };

  const handleMarkAttendance = () => {
    dispatch(markAttendance());
  };

  const handleFetchAttendance = () => {
    dispatch(fetchAttendance());
  };

  return (
    <div className="App">
      <h1 className="title">Facial Recognition Attendance System</h1>
      <RegisterFaceForm />
      <button className="btn" onClick={handleRegister}>Register Face</button>
      <button className="btn" onClick={handleMarkAttendance}>Mark Attendance</button>
      <button className="btn" onClick={handleFetchAttendance}>View Attendance</button>
      <p className="message">{message}</p>
      <ul className="attendance-list">
        {attendance.map((record, index) => (
          <li key={index}>{record[1]} marked attendance at {record[2]}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
