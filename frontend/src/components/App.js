import React from 'react';
import ReactDOM from 'react-dom';
import { addTodo } from '../actions/actions'
import { store } from '../store'
import { Provider } from 'react-redux'
import MainContainer from './MainContainer'


window.store = store
window.todo = {
	title: 'Movie time',
	description: 'Go watch Mission Impossible',
	completed: false,
	todolistid: 1
}
console.log(store.getState())
const unsubscribe = store.subscribe(() =>
  console.log(store.getState())
)
// store.dispatch(addTodo(todo))
unsubscribe()

const App = () => (
	<Provider store={store}>
		< MainContainer />
	</Provider>
)

document.addEventListener("DOMContentLoaded", () => {
	ReactDOM.render(<App />, document.getElementById("app"));
})