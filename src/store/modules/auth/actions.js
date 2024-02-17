export default{
    async login(context, payload){
        const response = await fetch('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyBZkOx5LWTOGe1JtDSwCND2h5SGGwSyp40',{
            method: 'POST',
            body: JSON.stringify({
                email: payload.email,
                password: payload.password,
                returnSecureToken: true
            })
        })

        const responseData = await response.json();

        if (!response.ok){
            const error = new Error(responseData.error.message || 'Failed to signup.')
            throw error;
        }
        
        localStorage.setItem('token', responseData.idToken);
        localStorage.setItem('user', responseData.localId);

        context.commit('setUser', {
            token: responseData.idToken,
            userId: responseData.localId,
            tokenExpiration: responseData.expiresIn
        })

    },

    async signup(context, payload){
        const response = await fetch('https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=AIzaSyBZkOx5LWTOGe1JtDSwCND2h5SGGwSyp40',{
            method: 'POST',
            body: JSON.stringify({
                email: payload.email,
                password: payload.password,
                returnSecureToken: true
            })
        })

        const responseData = await response.json();

        if (!response.ok){
            const error = new Error(responseData.error.message || 'Failed to signup.')
            throw error;
        }

        console.log(responseData)
        context.commit('setUser', {
            token: responseData.idToken,
            userId: responseData.localId,
            tokenExpiration: responseData.expiresIn
        })
    },
    logout(context){
        context.commit('setUser',{
            token: null,
            userId: null,
            tokenExpiration: null
        })
    }
}