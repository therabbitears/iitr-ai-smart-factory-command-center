import React, { createContext, useContext, useState } from 'react'

const AuthContext = createContext(null)

export function AuthProvider({children}){
  const [user, setUser] = useState(null)

  const login = async ({username, password}) => {
    // placeholder - integrate with real auth
    if(username && password){
      const u = {username}
      setUser(u)
      return u
    }
    throw new Error('Invalid credentials')
  }

  const logout = () => setUser(null)

  return (
    <AuthContext.Provider value={{user, login, logout}}>
      {children}
    </AuthContext.Provider>
  )
}

export function useAuth(){
  return useContext(AuthContext)
}
