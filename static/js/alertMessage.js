{% for message in messages %}
alertify.set('notifier', 'position', 'top-right');
{% if message.tags == 'error' %}
    alertify.error('{{ message }}');
{% else %}
    alertify.success('{{ message }}');
{% endif %}
{% endfor %}