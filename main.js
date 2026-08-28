document.addEventListener('DOMContentLoaded', function () {
    // Quantity stepper helper for cart / book detail
    document.querySelectorAll('.qty-stepper').forEach(function (stepper) {
        const input = stepper.querySelector('input[type="number"]');
        const minus = stepper.querySelector('.qty-minus');
        const plus = stepper.querySelector('.qty-plus');
        if (minus) minus.addEventListener('click', function () {
            let v = parseInt(input.value || '1', 10);
            if (v > parseInt(input.min || '1', 10)) input.value = v - 1;
        });
        if (plus) plus.addEventListener('click', function () {
            let v = parseInt(input.value || '1', 10);
            const max = input.max ? parseInt(input.max, 10) : Infinity;
            if (v < max) input.value = v + 1;
        });
    });

    // Payment method conditional fields on checkout
    const paymentRadios = document.querySelectorAll('input[name="payment_method"]');
    if (paymentRadios.length) {
        const toggleFields = function () {
            const selected = document.querySelector('input[name="payment_method"]:checked');
            document.querySelectorAll('.payment-fields').forEach(el => el.classList.add('d-none'));
            if (selected) {
                const target = document.getElementById('fields-' + selected.value);
                if (target) target.classList.remove('d-none');
            }
        };
        paymentRadios.forEach(r => r.addEventListener('change', toggleFields));
        toggleFields();
    }

    // Star rating input preview
    document.querySelectorAll('.star-select').forEach(function (container) {
        const stars = container.querySelectorAll('.star-choice');
        const hiddenSelect = document.getElementById(container.dataset.target);
        stars.forEach(function (star) {
            star.addEventListener('click', function () {
                const val = this.dataset.value;
                if (hiddenSelect) hiddenSelect.value = val;
                stars.forEach(s => s.classList.toggle('bi-star-fill', s.dataset.value <= val));
                stars.forEach(s => s.classList.toggle('bi-star', s.dataset.value > val));
            });
        });
    });
});
