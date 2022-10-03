import { configureStore } from '@reduxjs/toolkit'
import counterReducer from './counterSlice'
import auth from './auth'

export default configureStore({
  reducer: {
    counter: counterReducer,
    auth: auth,
  },
})
