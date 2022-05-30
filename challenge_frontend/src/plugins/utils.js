/**
 * Valida o PIS/PASEP
 * @param {string} pis
 *
 * @returns {boolean} true se o PIS/PASEP for válido
 */

export const pisValid = (pis) => {
  // function pisValid(pis) {
  var multiplicadorBase = "3298765432";
  var total = 0;
  var resto = 0;
  var multiplicando = 0;
  var multiplicador = 0;
  var digito = 99;

  // Retira a mascara
  var numeroPis = pis.replace(/[^\d]+/g, "");

  if (
    numeroPis.length !== 11 ||
    numeroPis === "00000000000" ||
    numeroPis === "11111111111" ||
    numeroPis === "22222222222" ||
    numeroPis === "33333333333" ||
    numeroPis === "44444444444" ||
    numeroPis === "55555555555" ||
    numeroPis === "66666666666" ||
    numeroPis === "77777777777" ||
    numeroPis === "88888888888" ||
    numeroPis === "99999999999"
  ) {
    return false;
  } else {
    for (var i = 0; i < 10; i++) {
      multiplicando = numeroPis.substring(i, i + 1);
      multiplicador = multiplicadorBase.substring(i, i + 1);
      total = total + multiplicando * multiplicador;
    }

    resto = 11 - (total % 11);
    resto = resto === 10 || resto === 11 ? 0 : resto;

    digito = parseInt("" + numeroPis.charAt(10));
    return resto === digito;
  }
};

/**
 * Valida o CPF
 * @param {string} cpf
 *
 * @return {boolean} cpfValido
 */
export const cpfValid = (cpf) => {
  if (cpf !== null && cpf !== undefined && cpf !== "") {
    cpf = cpf.replace(/[^\d]+/g, "");

    // Elimina CPFs invalidos conhecidos
    if (
      cpf.length != 11 ||
      cpf == "00000000000" ||
      cpf == "11111111111" ||
      cpf == "22222222222" ||
      cpf == "33333333333" ||
      cpf == "44444444444" ||
      cpf == "55555555555" ||
      cpf == "66666666666" ||
      cpf == "77777777777" ||
      cpf == "88888888888" ||
      cpf == "99999999999"
    )
      return false;

    // Valida 1º digito
    var add = 0;

    for (var i = 0; i < 9; i++) add += parseInt(cpf.charAt(i)) * (10 - i);

    var rev = 11 - (add % 11);

    if (rev == 10 || rev == 11) rev = 0;

    if (rev != parseInt(cpf.charAt(9))) return false;

    // Valida 2º digito
    add = 0;

    for (i = 0; i < 10; i++) add += parseInt(cpf.charAt(i)) * (11 - i);

    rev = 11 - (add % 11);

    if (rev == 10 || rev == 11) rev = 0;

    if (rev != parseInt(cpf.charAt(10))) return false;
  }

  return true;
};

/**
 * REGEX para validações
 *  */
export const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,20}$/;
export const emailRegex = /^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
