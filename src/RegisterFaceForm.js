import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { setName } from '../actions';
import './styles.css';

function RegisterFaceForm() {
  const dispatch = useDispatch();
  const name = useSelector(state => state.app.name);

  const handleNameChange = (e) => {
    dispatch(setName(e.target.value));
  };

  return (
    <div className="form">
      <input
        type="text"
        placeholder="Enter your name"
        value={name}
        onChange={handleNameChange}
        className="input-field"
      />
    </div>
  );
}

export default RegisterFaceForm;
