// Получаем данные из локального хранилища (если они там есть)
const storedEmployees = JSON.parse(localStorage.getItem('employees')) || [];

 // Инициализируем массив начальными данными
        const employees = storedEmployees.length > 0 ? storedEmployees : [
            { lastName: 'Иванов', firstName: 'Иван', middleName: 'Иванович', age: 25, experience: 3 },
            { lastName: 'Петров', firstName: 'Петр', middleName: 'Петрович', age: 30, experience: 4 },
            { lastName: 'Красовский', firstName: 'Валентин', middleName: 'Алексеевич', age: 20, experience: 4 },
            { lastName: 'Ласевич', firstName: 'Евгений', middleName: 'Викторович', age: 19, experience: 2 }
        ];
function addEmployee() {
    const lastName = document.getElementById('lastName').value;
    const firstName = document.getElementById('firstName').value;
    const middleName = document.getElementById('middleName').value;
    const age = parseInt(document.getElementById('age').value);
    const experience = parseInt(document.getElementById('experience').value);

    if (!isNaN(age) && !isNaN(experience)) {
        employees.push({ lastName, firstName, middleName, age, experience });
        saveDataToLocalstorage(); // Сохраняем данные в локальное хранилище

        // Очистим поля ввода
        document.getElementById('lastName').value = '';
        document.getElementById('firstName').value = '';
        document.getElementById('middleName').value = '';
        document.getElementById('age').value = '';
        document.getElementById('experience').value = '';

        alert('Сотрудник добавлен!');
    } else {
        alert('Введите корректные данные для возраста и стажа.');
    }
}

function findYoungestEmployees() {
    const resultElement = document.getElementById('result');
    resultElement.innerHTML = '<h2>Результат:</h2>';

    const filteredEmployees = employees.filter(employee => employee.age <= 30 && employee.experience >= 3);

    if (filteredEmployees.length > 0) {
        filteredEmployees.forEach(employee => {
            console.log(employee);
            resultElement.innerHTML += `<p>${employee.lastName} ${employee.firstName} ${employee.middleName}, возраст: ${employee.age}, стаж: ${employee.experience} лет</p>`;
        });
    } else {
        resultElement.innerHTML += '<p>Нет сотрудников, удовлетворяющих условиям.</p>';
    }
}
 // Сохраняем данные в локальное хранилище
    function saveDataToLocalstorage() {
        localStorage.setItem('employees', JSON.stringify(employees));
    }