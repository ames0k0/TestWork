import { createSlice } from '@reduxjs/toolkit'

export const auth = createSlice({
  name: 'auth',
  initialState: {
    name: '',
    email: '',
    passwd: '',
    admin: 0,
    loggedin: 0,
  },
  reducers: {
    setName: (state, target) => {
      state.name = target;
      console.log("target:", target, "name:", state.name);
    },
    setEmail: (state, target) => {
      state.email = target;
    },
    setPasswd: (state, target) => {
      state.passwd = target;
    },
    login: (state) => {
      if ((state.name === 'admin') && (state.passwd === '123')) {
        state.admin += 1;
      }
      state.loggedin += 1;
    }
  },
})

// Action creators are generated for each case reducer function
export const { setName, setEmail, setPasswd, login } = auth.actions

export default auth.reducer
