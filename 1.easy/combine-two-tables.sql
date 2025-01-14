SELECT
    person.firstname,
    person.lastname,
    address.city,
    address.state
FROM Person person
LEFT JOIN Address address
    ON person.personId = address.personId