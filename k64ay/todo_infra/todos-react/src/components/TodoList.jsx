import React from 'react';
import PropTypes from 'prop-types';

import styles from './Todos.module.scss';
import Header from './Header';
import InputTodo from './InputTodo';
import TodoItem from './TodoItem';


const TodoList = ({ todos, addTodo, updateTodo, deleteTodo }) => {

    return (
        <div className={styles.container}>
            <div className="inner">
                <Header />
                <InputTodo addTodo={addTodo} />
                <ul>
                    {todos.map((todo) => (
                        <TodoItem
                            key={todo.id}
                            todo={todo}
                            deleteTodo={deleteTodo}
                            updateTodo={updateTodo}
                        />
                    ))}
                </ul>
            </div>
        </div>
    );
};

TodoList.propTypes = {
    todos: PropTypes.array.isRequired,
    addTodo: PropTypes.func.isRequired,
    updateTodo: PropTypes.func.isRequired,
    deleteTodo: PropTypes.func.isRequired,
};

export default TodoList;
