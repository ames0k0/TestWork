import React from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { login, setName, setEmail, setPasswd } from './auth'


export default function Counter() {
  const loggedin = useSelector((state) => state.auth.loggedin);
  // const email = useSelector((state) => state.email.value)
  // const passwd = useSelector((state) => state.passwd.value)
  const dispatch = useDispatch();

  function FormView(props) {
    return (
      <div>
        <form>
          <input placeholder="Name" name="name"
            autoComplete="off"
            onChange={(event) => dispatch(setName(event.target.value))}
            />
          <input placeholder="Email" name="email"
            autoComplete="off"
            onChange={(event) => dispatch(setEmail(event.target.value))}
            />
          <input placeholder="Password: Not required" name="passwd"
            autoComplete="off"
            onChange={(event) => dispatch(setPasswd(event.target.value))}
            />
          <button
            aria-label="Login"
            onClick={() => dispatch(login())}
          >
            Login
          </button>
        </form>
      </div>
    );
  }

  function TodoList(props) {
    // actions -> component ?
    return (
      <div className="todo-list">

        <div className="actions">
          <div className="filters">
            <button>Name</button>
            <button>Email</button>
            <button>Status</button>
          </div>
        </div>

        <div className="list">

          <div className="list-item">Add new only on the first pagination ??
            <p>
              <span><input type="checkbox" onClick="OWN-or-ADMIN"/></span>
              <span>User name (get name) </span>
            </p>
            <p>User email (get email) </p>
            <input placeholder="new todo" />
            <button>Add</button>
            <button>Clear</button>

          </div>

          <div className="list-item">
            <p>
              <span><input type="checkbox" onClick="OWN-or-ADMIN"/></span>
              <span>User name</span>
            </p>
            <p>User email</p>
            <p>tesfjesfj eefj[eifjoiefjei fj pwoifjwoeifj</p>
          </div>

        </div>

        <div className="pagination">
        </div>

      </div>
    );
  }

  // onChange={(event) => onChange(event.target.value
  // const onSubmit = data => console.log(data);

// {isLoggedIn ? (
//   <LogoutButton onClick={this.handleLogoutClick} />
// ) : (
//   <LoginButton onClick={this.handleLoginClick} />
// )}

  console.log(loggedin);
  return (
    <div>
      {(loggedin === 0) ? <FormView /> : <TodoList />}
    </div>
  )
}

