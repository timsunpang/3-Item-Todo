import { connect } from 'react-redux'
import { getTodos } from '../actions/actions'
import Main from './Main'

const mapStateToProps = state => {
	return {
		todos: state.todos,
		currentTodo: state.currentTodo
	}
}

const mapDispatchToProps = dispatch => {
	return {
		getTodos: () => {dispatch(getTodos())}
	}
}

const MainContainer = connect(
	mapStateToProps,
	mapDispatchToProps,
)(Main)

export default MainContainer