import '@/styles/globals.css'
import * as React from "react";
import { ChakraProvider, extendTheme, Flex, Box } from "@chakra-ui/react";


const theme = extendTheme({
  config: {
    initialColorMode: "light",
    useSystemColorMode: false,
  },
});

export default function App({ Component, pageProps }) {
  return(
    <ChakraProvider theme={theme}>
          <Flex direction="column" minH="100vh">
            <Box as="header">
            </Box>
            <Flex as="main" direction="column" flex="1" overflow="hidden">
              <Component {...pageProps} />
            </Flex>
          </Flex>
    </ChakraProvider>
  ); 
}