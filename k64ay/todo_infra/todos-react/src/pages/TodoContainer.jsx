import React, { useEffect, useState } from 'react';

import api from '../utils/api';
import TodoList from '../components/TodoList';


const TodoContainer = () => {

    const [todos, setTodos] = useState([]);

    const addTodo = async (desc) => {
        const { data } = await api.post('/tasks/', {
            desc: desc,
            done: false
        })
        console.log(data);
        setTodos([...todos, data]);
    };

    const deleteTodo = async (id) => {
        await api.delete(`/tasks/${id}/`);
        setTodos([...todos.filter((todo) => todo.id !== id)]);
    };

    const updateTodo = async (updatedTodo) => {
        await api.put(`/tasks/${updatedTodo.id}/`, updatedTodo);

        setTodos(
            todos.map((todo) => {
                if (todo.id === updatedTodo.id) {
                    todo = { ...todo, ...updatedTodo };
                }
                return todo;
            }),
        );
    };

    useEffect(() => {
        async function fetchData() {
            const { data } = await api.get('/tasks/');
            console.log(data)
            setTodos(data);
        }

        fetchData()

    }, []);

    return (
        <TodoList 
            todos={todos}
            addTodo={addTodo}
            updateTodo={updateTodo}
            deleteTodo={deleteTodo}
        />
    );
};

export default TodoContainer;
