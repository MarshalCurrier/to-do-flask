export default function Home(){
    return (
        <>
            <body class="bg-gray-100">
                <div id="app" class="container mx-auto px-4 py-8">
                    <header class="mb-8">
                        <h1 class="text-4xl font-bold text-center text-blue-600">SharedTodo</h1>
                        <p class="text-center text-gray-600 mt-2">Collaborate, Share, and Get Things Done</p>
                    </header>

        <nav class="mb-8 flex justify-center space-x-4">
            <a href="#" class="text-blue-500 hover:text-blue-700">Login</a>
            <a href="#" class="text-blue-500 hover:text-blue-700" >Sign Up</a>
            <a href="#" class="text-blue-500 hover:text-blue-700">Logout</a>
        </nav>

        <main>
            <section v-if="!isLoggedIn" class="text-center">
                <h2 class="text-2xl font-semibold mb-4">Welcome to SharedTodo</h2>
                <p class="mb-4">Join our community to start sharing and managing tasks with friends, family, and colleagues.</p>
                <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                    Get Started
                </button>
            </section>

            <section v-if="isLoggedIn" class="bg-white shadow-md rounded-lg p-6">
                <h2 class="text-2xl font-semibold mb-4">My To-Do Lists</h2>
                <ul class="space-y-2">
                    <li v-for="list in todoLists" class="flex items-center justify-between">
                        <button class="text-blue-500 hover:text-blue-700">View</button>
                    </li>
                </ul>
                <button class="mt-4 bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                    Create New List
                </button>
            </section>
        </main>

        <div v-if="showLoginModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full">
            <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                <h3 class="text-lg font-semibold mb-4">Login</h3>
                <div>
                    <input type="email" v-model="loginEmail" placeholder="Email" class="w-full p-2 mb-4 border rounded"/>
                    <input type="password" v-model="loginPassword" placeholder="Password" class="w-full p-2 mb-4 border rounded"/>
                    <button type="submit" class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
                        Login
                    </button>
                </div>
                <button class="mt-4 text-sm text-gray-600 hover:text-gray-800">Close</button>
            </div>
        </div>

        <div v-if="showSignupModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full">
            <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                <h3 class="text-lg font-semibold mb-4">Sign Up</h3>
                <form>
                    <input type="text" v-model="signupName" placeholder="Full Name" class="w-full p-2 mb-4 border rounded" required/>
                    <input type="email" v-model="signupEmail" placeholder="Email" class="w-full p-2 mb-4 border rounded" required/>
                    <input type="password" v-model="signupPassword" placeholder="Password" class="w-full p-2 mb-4 border rounded" required/>
                    <input type="tel" v-model="signupPhone" placeholder="Phone (optional)" class="w-full p-2 mb-4 border rounded"/>
                    <button type="submit" class="w-full bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                        Sign Up
                    </button>
                </form>
                <button class="mt-4 text-sm text-gray-600 hover:text-gray-800">Close</button>
            </div>
        </div>

        <div v-if="showCreateListModal" class="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full">
            <div class="relative top-20 mx-auto p-5 border w-96 shadow-lg rounded-md bg-white">
                <h3 class="text-lg font-semibold mb-4">Create New To-Do List</h3>
                <form>
                    <input type="text" v-model="newListName" placeholder="List Name" class="w-full p-2 mb-4 border rounded" required/>
                    <button type="submit" class="w-full bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">
                        Create List
                    </button>
                </form>
                <button class="mt-4 text-sm text-gray-600 hover:text-gray-800">Close</button>
            </div>
        </div>
    </div>

</body>
        </>
    )
}